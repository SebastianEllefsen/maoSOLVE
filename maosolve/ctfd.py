import shutil
import subprocess
import sys


def fetch_challenges(url: str, session: str, out: str = "challdump") -> None:
    if not shutil.which("ctfdget"):
        print("Error: 'ctfdget' not found. Install it:")
        print("  go install github.com/HanEmile/ctfdget@latest")
        sys.exit(1)

    cmd = [
        "ctfdget",
        "-url", url,
        "-session", session,
        "-out", out,
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running ctfdget: {e}")
        sys.exit(1)
