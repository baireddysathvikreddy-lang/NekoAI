"""Desktop app launcher for Roblox Studio and Unreal Engine."""

from __future__ import annotations

import os
import subprocess
import platform
from pathlib import Path
from typing import Optional


class StudioLauncher:
    """Intelligently launches and manages game engine studios."""

    def __init__(self):
        self.os_type = platform.system()  # Windows, Darwin (Mac), Linux
        self.roblox_path = self._find_roblox_studio()
        self.unreal_path = self._find_unreal_engine()

    def _find_roblox_studio(self) -> Optional[str]:
        """Locate Roblox Studio installation."""
        if self.os_type == "Windows":
            # Check common install locations
            common_paths = [
                Path(os.getenv("LOCALAPPDATA", "")) / "Roblox" / "Versions",
                Path("C:/Program Files (x86)/Roblox/Versions"),
            ]
            for base_path in common_paths:
                if base_path.exists():
                    # Find the latest version
                    versions = sorted(base_path.glob("version-*"))
                    if versions:
                        return str(versions[-1] / "RobloxStudioBeta.exe")
        elif self.os_type == "Darwin":
            mac_path = Path("/Applications/Roblox Studio.app/Contents/MacOS/Roblox Studio")
            if mac_path.exists():
                return str(mac_path)
        return None

    def _find_unreal_engine(self) -> Optional[str]:
        """Locate Unreal Engine installation."""
        if self.os_type == "Windows":
            common_paths = [
                Path("C:/Program Files/Epic Games"),
                Path(os.getenv("PROGRAMFILES", "")) / "Epic Games",
            ]
            for base_path in common_paths:
                if base_path.exists():
                    # Find UE5 or UE4
                    for engine in sorted(base_path.glob("UE_*"), reverse=True):
                        exe = engine / "Engine" / "Binaries" / "Win64" / "UnrealEditor.exe"
                        if exe.exists():
                            return str(exe)
        elif self.os_type == "Darwin":
            mac_path = Path("/Users/Shared/Epic Games")
            if mac_path.exists():
                for engine in sorted(mac_path.glob("UE_*"), reverse=True):
                    exe = engine / "Engine" / "Binaries" / "Mac" / "UE4Editor"
                    if exe.exists():
                        return str(exe)
        return None

    def open_roblox_studio(self, project_file: Optional[str] = None) -> bool:
        """Launch Roblox Studio, optionally opening a project file."""
        if not self.roblox_path:
            print("❌ Roblox Studio not found. Please install it from roblox.com/create")
            return False

        try:
            if project_file and os.path.exists(project_file):
                subprocess.Popen([self.roblox_path, project_file])
            else:
                subprocess.Popen([self.roblox_path])
            print(f"✅ Opened Roblox Studio" + (f" with {project_file}" if project_file else ""))
            return True
        except Exception as e:
            print(f"❌ Failed to open Roblox Studio: {e}")
            return False

    def open_unreal_engine(self, project_file: Optional[str] = None) -> bool:
        """Launch Unreal Engine, optionally opening a project."""
        if not self.unreal_path:
            print("❌ Unreal Engine not found. Please install it from unrealengine.com")
            return False

        try:
            if project_file and os.path.exists(project_file):
                subprocess.Popen([self.unreal_path, project_file])
            else:
                subprocess.Popen([self.unreal_path])
            print(f"✅ Opened Unreal Engine" + (f" with {project_file}" if project_file else ""))
            return True
        except Exception as e:
            print(f"❌ Failed to open Unreal Engine: {e}")
            return False

    def open_youtube(self, query: Optional[str] = None) -> bool:
        """Open YouTube, optionally search for something."""
        try:
            url = "https://www.youtube.com"
            if query:
                # URL encode the search query
                search_query = query.replace(" ", "+")
                url = f"https://www.youtube.com/results?search_query={search_query}"

            if self.os_type == "Windows":
                os.startfile(url)
            elif self.os_type == "Darwin":
                subprocess.Popen(["open", url])
            elif self.os_type == "Linux":
                subprocess.Popen(["xdg-open", url])

            print(f"✅ Opened YouTube" + (f" searching for '{query}'" if query else ""))
            return True
        except Exception as e:
            print(f"❌ Failed to open YouTube: {e}")
            return False

    def open_browser(self, url: str) -> bool:
        """Open a URL in the default browser."""
        try:
            if self.os_type == "Windows":
                os.startfile(url)
            elif self.os_type == "Darwin":
                subprocess.Popen(["open", url])
            elif self.os_type == "Linux":
                subprocess.Popen(["xdg-open", url])

            print(f"✅ Opened browser: {url}")
            return True
        except Exception as e:
            print(f"❌ Failed to open browser: {e}")
            return False


__all__ = ["StudioLauncher"]
