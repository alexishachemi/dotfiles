import json
import os.path as osp

ROOT = osp.join(osp.dirname(__file__), "..")
CONFIG_NAME = "config.json"
TRACKED_NAME = ".tracked"
TRACKED_DIR = "tracked"

CONFIG_PATH = osp.abspath(osp.join(ROOT, CONFIG_NAME))
TRACKED_PATH = osp.abspath(osp.join(ROOT, TRACKED_NAME))

DEFAULT_CONFIG = { "packages": {}, "configs": [] }

def read_config() -> dict:
    if not osp.isfile(CONFIG_PATH):
        return DEFAULT_CONFIG
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def write_config(config: dict) -> None:
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)


def read_tracked() -> dict:
    if not osp.isfile(TRACKED_PATH):
        return {}
    try:
        with open(TRACKED_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def write_tracked(tracked: list[str]) -> None:
    tracked_dict: dict = {osp.basename(path): path for path in tracked}
    with open(TRACKED_PATH, "w") as f:
        json.dump(tracked_dict, f)
