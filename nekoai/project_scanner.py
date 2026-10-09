"""Smart project scanner that understands Roblox and Unreal projects."""

from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Dict, List, Any, Optional


class ProjectScanner:
    """Scans project directories and understands structure, dependencies, and current state."""

    def __init__(self):
        self.project_info: Dict[str, Any] = {}

    def scan_roblox_project(self, project_path: str) -> Dict[str, Any]:
        """
        Scan a Roblox project and extract structure, scripts, models, etc.
        Looks for .rbxl, .rbxm files and ServerScriptService, LocalScriptService structure.
        """
        path = Path(project_path)
        if not path.exists():
            return {"error": f"Path {project_path} does not exist"}

        project_data = {
            "type": "roblox",
            "path": str(path),
            "name": path.name,
            "files": [],
            "scripts": {
                "server": [],
                "client": [],
                "shared": [],
                "modulescripts": [],
            },
            "models": [],
            "assets": [],
            "rbxl_files": [],
            "has_datastore": False,
            "has_networking": False,
            "has_custom_classes": False,
        }

        try:
            # Walk through directory
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = Path(root) / file
                    rel_path = str(file_path.relative_to(path))

                    # Roblox project file
                    if file.endswith(".rbxl") or file.endswith(".rbxm"):
                        project_data["rbxl_files"].append(rel_path)

                    # Script files
                    elif file.endswith(".lua") or file.endswith(".luau"):
                        content = self._read_file_safe(file_path)
                        if content:
                            self._classify_lua_script(content, rel_path, project_data)

                    # Config/metadata
                    elif file == "studio.json" or file == "metadata.json":
                        config = self._read_json_safe(file_path)
                        if config:
                            project_data.update(config)

                    # All files tracked
                    project_data["files"].append(rel_path)

        except Exception as e:
            project_data["scan_error"] = str(e)

        self.project_info = project_data
        return project_data

    def scan_unreal_project(self, project_path: str) -> Dict[str, Any]:
        """
        Scan an Unreal Engine project and extract C++/Blueprint structure.
        Looks for .uproject, Source/, Blueprints/, Content/ folders.
        """
        path = Path(project_path)
        if not path.exists():
            return {"error": f"Path {project_path} does not exist"}

        project_data = {
            "type": "unreal",
            "path": str(path),
            "name": path.name,
            "uproject_file": None,
            "cpp_classes": [],
            "blueprints": [],
            "plugins": [],
            "content": [],
            "has_cpp": False,
            "has_blueprints": False,
            "engine_version": None,
        }

        try:
            # Find .uproject file
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = Path(root) / file
                    rel_path = str(file_path.relative_to(path))

                    # Project file
                    if file.endswith(".uproject"):
                        project_data["uproject_file"] = rel_path
                        config = self._read_json_safe(file_path)
                        if config:
                            project_data["engine_version"] = config.get("EngineAssociation", "Unknown")
                            project_data["plugins"] = config.get("Plugins", [])

                    # C++ files
                    elif file.endswith(".cpp") or file.endswith(".h"):
                        if "Source/" in rel_path:
                            project_data["cpp_classes"].append(rel_path)
                            project_data["has_cpp"] = True

                    # Blueprints
                    elif file.endswith(".uasset") and "Blueprints/" in rel_path:
                        project_data["blueprints"].append(rel_path)
                        project_data["has_blueprints"] = True

                    # Content
                    elif "Content/" in rel_path:
                        project_data["content"].append(rel_path)

        except Exception as e:
            project_data["scan_error"] = str(e)

        self.project_info = project_data
        return project_data

    def _classify_lua_script(self, content: str, file_path: str, project_data: Dict) -> None:
        """Classify Lua scripts by their purpose and location."""
        content_lower = content.lower()

        # Detect what the script does
        if "datastore" in content_lower or "datastoreservice" in content_lower:
            project_data["has_datastore"] = True

        if "remoteevent" in content_lower or "remotefunction" in content_lower:
            project_data["has_networking"] = True

        if "class" in content_lower or "function " in content_lower and "self" in content_lower:
            project_data["has_custom_classes"] = True

        # Classify by file location or naming
        if "server" in file_path.lower() or "serverscriptservice" in file_path.lower():
            project_data["scripts"]["server"].append(file_path)
        elif "client" in file_path.lower() or "localscriptservice" in file_path.lower():
            project_data["scripts"]["client"].append(file_path)
        elif "module" in file_path.lower():
            project_data["scripts"]["modulescripts"].append(file_path)
        else:
            project_data["scripts"]["shared"].append(file_path)

    def _read_file_safe(self, file_path: Path, max_size: int = 100000) -> Optional[str]:
        """Safely read file content, limiting size to avoid huge files."""
        try:
            if file_path.stat().st_size > max_size:
                return None
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception:
            return None

    def _read_json_safe(self, file_path: Path) -> Optional[Dict]:
        """Safely read JSON file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def get_project_summary(self) -> str:
        """Generate a human-readable summary of the scanned project."""
        if not self.project_info:
            return "No project scanned yet."

        info = self.project_info
        project_type = info.get("type", "unknown").upper()
        name = info.get("name", "Unknown")

        if project_type == "ROBLOX":
            server_scripts = len(info.get("scripts", {}).get("server", []))
            client_scripts = len(info.get("scripts", {}).get("client", []))
            modules = len(info.get("scripts", {}).get("modulescripts", []))

            summary = f"""
📁 **Roblox Project: {name}**
- **Server Scripts**: {server_scripts}
- **Client Scripts**: {client_scripts}
- **Module Scripts**: {modules}
- **Has DataStore**: {info.get('has_datastore', False)}
- **Has Networking**: {info.get('has_networking', False)}
- **Has Custom Classes**: {info.get('has_custom_classes', False)}
- **Total Files**: {len(info.get('files', []))}
            """

        elif project_type == "UNREAL":
            cpp_files = len(info.get("cpp_classes", []))
            blueprints = len(info.get("blueprints", []))
            engine_version = info.get("engine_version", "Unknown")

            summary = f"""
📁 **Unreal Engine Project: {name}**
- **Engine Version**: {engine_version}
- **C++ Classes**: {cpp_files}
- **Blueprints**: {blueprints}
- **Has C++**: {info.get('has_cpp', False)}
- **Has Blueprints**: {info.get('has_blueprints', False)}
- **Content Files**: {len(info.get('content', []))}
            """

        else:
            summary = f"📁 Unknown project type at {info.get('path', 'unknown')}"

        return summary


__all__ = ["ProjectScanner"]
