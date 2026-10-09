"""Activity watcher that monitors what the developer is doing in real-time."""

from __future__ import annotations

import time
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
import threading


class ActivityEvent:
    """Represents a single activity/action the developer takes."""

    def __init__(self, event_type: str, details: Dict[str, Any]):
        self.type = event_type  # "file_created", "file_modified", "script_added", etc.
        self.details = details
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "timestamp": self.timestamp,
            "details": self.details,
        }


class ActivityWatcher:
    """
    Watches developer activity in Roblox/Unreal projects.
    Tracks: file changes, script additions, structure changes, build actions.
    Feeds observations into the AI for intelligent code generation.
    """

    def __init__(self, project_path: str, project_type: str = "roblox"):
        self.project_path = Path(project_path)
        self.project_type = project_type  # "roblox" or "unreal"
        self.activity_log: List[ActivityEvent] = []
        self.callbacks: List[Callable[[ActivityEvent], None]] = []
        self.is_watching = False
        self.file_states: Dict[str, float] = {}  # Track file modification times
        self.watch_thread: Optional[threading.Thread] = None

    def register_callback(self, callback: Callable[[ActivityEvent], None]) -> None:
        """Register a callback to be called when activity is detected."""
        self.callbacks.append(callback)

    def start_watching(self, poll_interval: float = 2.0) -> None:
        """Start watching for file changes and developer actions."""
        self.is_watching = True
        self.watch_thread = threading.Thread(
            target=self._watch_loop,
            args=(poll_interval,),
            daemon=True,
        )
        self.watch_thread.start()
        print(f"🐱 NekoAI is watching your {self.project_type} project...")

    def stop_watching(self) -> None:
        """Stop watching for changes."""
        self.is_watching = False
        if self.watch_thread:
            self.watch_thread.join(timeout=5)
        print("🐱 NekoAI stopped watching.")

    def _watch_loop(self, poll_interval: float) -> None:
        """Main watch loop that runs in a separate thread."""
        while self.is_watching:
            try:
                self._scan_for_changes()
                time.sleep(poll_interval)
            except Exception as e:
                print(f"⚠️ Watch error: {e}")
                time.sleep(poll_interval)

    def _scan_for_changes(self) -> None:
        """Scan project directory for file changes and new files."""
        try:
            for root, dirs, files in self.project_path.walk():
                for file in files:
                    file_path = Path(root) / file

                    # Skip certain files
                    if self._should_ignore_file(file_path):
                        continue

                    # Check if file is new or modified
                    try:
                        mtime = file_path.stat().st_mtime
                        prev_mtime = self.file_states.get(str(file_path))

                        if prev_mtime is None:
                            # New file detected
                            self._emit_event(
                                "file_created",
                                {
                                    "path": str(file_path.relative_to(self.project_path)),
                                    "name": file,
                                    "size": file_path.stat().st_size,
                                },
                            )
                        elif mtime > prev_mtime:
                            # File modified
                            self._emit_event(
                                "file_modified",
                                {
                                    "path": str(file_path.relative_to(self.project_path)),
                                    "name": file,
                                },
                            )

                        self.file_states[str(file_path)] = mtime
                    except OSError:
                        pass

        except Exception as e:
            print(f"⚠️ Scan error: {e}")

    def _should_ignore_file(self, file_path: Path) -> bool:
        """Check if a file should be ignored."""
        ignore_patterns = [
            ".git",
            "__pycache__",
            ".pyc",
            "node_modules",
            ".lock",
            "temp",
            "cache",
        ]
        return any(pattern in str(file_path) for pattern in ignore_patterns)

    def _emit_event(self, event_type: str, details: Dict[str, Any]) -> None:
        """Create an activity event and notify all callbacks."""
        event = ActivityEvent(event_type, details)
        self.activity_log.append(event)

        # Call all registered callbacks
        for callback in self.callbacks:
            try:
                callback(event)
            except Exception as e:
                print(f"⚠️ Callback error: {e}")

    def analyze_recent_activity(self, last_n: int = 10) -> Dict[str, Any]:
        """Analyze recent activity to understand what the developer is building."""
        recent = self.activity_log[-last_n:]

        analysis = {
            "total_events": len(recent),
            "file_creates": 0,
            "file_modifies": 0,
            "lua_scripts": 0,
            "cpp_files": 0,
            "blueprints": 0,
            "recent_files": [],
            "inferred_work": "",
        }

        for event in recent:
            if event.type == "file_created":
                analysis["file_creates"] += 1
                file_path = event.details.get("path", "")
                analysis["recent_files"].append(file_path)

                if file_path.endswith(".lua") or file_path.endswith(".luau"):
                    analysis["lua_scripts"] += 1
                elif file_path.endswith(".cpp") or file_path.endswith(".h"):
                    analysis["cpp_files"] += 1
                elif file_path.endswith(".uasset"):
                    analysis["blueprints"] += 1

            elif event.type == "file_modified":
                analysis["file_modifies"] += 1
                analysis["recent_files"].append(event.details.get("path", ""))

        # Infer what they're working on
        if analysis["lua_scripts"] > 0:
            analysis["inferred_work"] = "Building Roblox game systems (Lua scripts)"
        elif analysis["cpp_files"] > 0:
            analysis["inferred_work"] = "Writing Unreal Engine C++ code"
        elif analysis["blueprints"] > 0:
            analysis["inferred_work"] = "Creating Unreal blueprints and game mechanics"

        return analysis

    def get_activity_summary(self) -> str:
        """Get a human-readable summary of all activity."""
        if not self.activity_log:
            return "No activity recorded yet."

        analysis = self.analyze_recent_activity(last_n=len(self.activity_log))

        summary = f"""
🐱 **NekoAI Activity Report**
- **Total Events**: {analysis['total_events']}
- **Files Created**: {analysis['file_creates']}
- **Files Modified**: {analysis['file_modifies']}
- **Lua Scripts**: {analysis['lua_scripts']}
- **C++ Files**: {analysis['cpp_files']}
- **Blueprints**: {analysis['blueprints']}
- **Current Work**: {analysis['inferred_work']}
- **Recent Files**: {', '.join(analysis['recent_files'][:5])}
        """
        return summary


__all__ = ["ActivityWatcher", "ActivityEvent"]
