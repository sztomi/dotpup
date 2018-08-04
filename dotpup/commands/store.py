from pathlib import Path
from os import makedirs

from dotpup.utils import symlink, get_repo_path

import dotpup.output as output

from .base import BaseCommand


class StoreCommand(BaseCommand):
  def __init__(self):
    super().__init__(
        name="store",
        desc="Moves a file to the repository, creates a symlink in place "
        "of the original and records the operation")
    self.parser.add_argument("target_file")
    #self.parser.add_argument("repo_file")

  def run(self, args):
    import shutil
    import platform
    import dotpup.config as config
    from dotpup.utils import unexpand, remove_prefix, get_repo_path

    # Move to repo and symlink back
    repo = get_repo_path()
    target_file = str(Path(args.target_file).resolve())
    repo_file = Path(f"{repo}/{remove_prefix(target_file)}")
    print(f"Moving {target_file} to {repo_file}")
    makedirs(repo_file.parent, exist_ok=True)
    shutil.move(args.target_file, repo_file)
    print(f"Linking {repo_file} to {target_file}")
    symlink(repo_file, target_file)

    cfg = config.load_config()
    if "operations" not in cfg:
      cfg["operations"] = {}

    dst = remove_prefix(target_file)
    os_name = platform.system()
    if os_name not in cfg["operations"]:
      cfg["operations"][os_name] = {}
    cfg["operations"][os_name][dst] = unexpand(target_file)
    config.save_config(cfg)

    return 0


command = StoreCommand()
