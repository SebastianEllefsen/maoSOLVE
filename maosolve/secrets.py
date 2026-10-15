import json
import shutil
import subprocess
import sys


def get_ctfd_session(env: str = "dev", project_id: str | None = None) -> str:
    """Fetch the CTFD_SESSION secret from Infisical."""
    if not shutil.which("infisical"):
        print("Error: 'infisical' CLI not found. Install it: https://infisical.com/docs/cli/overview")
        sys.exit(1)

    cmd = [
        "infisical", "secrets", "get", "CTFD_SESSION",
        "--env", env,
        "--plain",
    ]
    if project_id:
        cmd.extend(["--projectId", project_id])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        value = result.stdout.strip()
        if not value:
            print("Error: CTFD_SESSION secret is empty in Infisical.")
            sys.exit(1)
        return value
    except subprocess.CalledProcessError as e:
        print(f"Error fetching secret from Infisical: {e.stderr.strip()}")
        sys.exit(1)
