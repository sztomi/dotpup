import os
import platform

from pathlib import Path

import dotpup.config as config


def get_repo_path(filepath: Path) -> Path:
  def find_up(path):
    last_dir = path.parent
    current_dir = last_dir
    while True:
      full_path = (current_dir / path).resolve(strict=False)
      if full_path.exists():
        return full_path
      last_dir = current_dir
      current_dir = current_dir.parent
      if last_dir == current_dir:
        return None
  return find_up(filepath)


def unexpand(expanded: str, env_var: str = "HOME") -> str:
  def shellify_var(var_name: str) -> str:
    if platform.system() == "Windows":
      return f"%{var_name}%"
    else:
      return f"${var_name}"
  val = os.environ[env_var]
  return expanded.replace(val, shellify_var(env_var))


def symlink(src: Path, dst: Path, record=True):
  system = platform.system()
  if system != "Windows":
    os.symlink(src, dst)
  else:
    raise NotImplementedError()


