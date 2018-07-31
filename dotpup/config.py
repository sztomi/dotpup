import json

from dotpup.utils import get_repo_path

config_filename = "dotpup.json"


def _conf_path():
  return get_repo_path(config_filename) / config_filename


def load_config():
  with open(_conf_path()) as cfg:
    return json.load(cfg)


def save_config(cfg_data: dict):
  with open(_conf_path(), "w") as cfg:
    json.dump(cfg_data, cfg, sort_keys=True, indent=2)
