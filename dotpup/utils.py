import os
import platform

from pathlib import Path

from . import config


def get_repo_path() -> Path:
  return Path(os.getenv("DOTPUP_HOME"))


def shellify_var(var_name: str) -> str:
  if platform.system() == "Windows":
    return f"%{var_name}%"
  else:
    return f"${var_name}"


def unexpand(filepath: str, env_var="HOME") -> str:
  val = os.getenv(env_var)
  return filepath.replace(val, shellify_var(env_var))


def remove_prefix(filepath: str, env_var="HOME") -> str:
  val = os.getenv(env_var)
  unprefixed = filepath.replace(val, "")
  if unprefixed[0] in ("/", "\\"):
    unprefixed = unprefixed[1:]
  return unprefixed


def symlink(src: Path, dst: Path, record=True):
  system = platform.system()
  if system != "Windows":
    os.symlink(src, dst)
  else:
    raise NotImplementedError()
