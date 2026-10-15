import os
import sys
import tomllib

CONFIG_NAME = "maosolve.toml"

DEFAULT_CONFIG = """\
[maosolve]
flag_format = ""
ctf_url = ""
output_dir = "challdump"

[infisical]
env = "dev"
project_id = ""
"""


def config_path() -> str:
    return os.path.join(os.getcwd(), CONFIG_NAME)


def create_default_config() -> str:
    path = config_path()
    with open(path, "w") as f:
        f.write(DEFAULT_CONFIG)
    return path


def load_config() -> dict:
    path = config_path()
    if not os.path.exists(path):
        return {}
    with open(path, "rb") as f:
        return tomllib.load(f)


def get(key: str, section: str = "maosolve") -> str:
    cfg = load_config()
    return cfg.get(section, {}).get(key, "")
