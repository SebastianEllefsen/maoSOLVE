import os
import shutil
import subprocess
import sys


def scan_for_flags(directory: str, flag_format: str) -> list[tuple[str, str]]:
    if not shutil.which("stringcheese"):
        print("Error: 'stringcheese' not found. Install it:")
        print("  pip install stringcheese")
        sys.exit(1)

    if not os.path.isdir(directory):
        print(f"Error: directory '{directory}' does not exist.")
        sys.exit(1)

    found: list[tuple[str, str]] = []

    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                result = subprocess.run(
                    ["stringcheese", flag_format, "--file", path],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                for line in result.stdout.strip().splitlines():
                    line = line.strip()
                    if line:
                        found.append((path, line))
            except subprocess.TimeoutExpired:
                continue
            except Exception:
                continue

    return found
