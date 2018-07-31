from pathlib import Path
from .base import BaseCommand

from dotpup.utils import symlink

import dotpup.output as output


class StoreCommand(BaseCommand):
  def __init__(self):
    super().__init__(
      name="store",
      desc="Moves a file to the repository, creates a symlink in place "
           "of the original and records the operation")
    self.parser.add_argument("target_file")
    self.parser.add_argument("repo_file")

  def run(self, args):
    import shutil
    import dotpup.config as config
    from dotpup.utils import unexpand

    shutil.move(args.target_file, args.repo_file)
    symlink(args.repo_file, args.target_file)

    cfg = config.load_config()
    if "operations" not in cfg:
      cfg["operations"] = {}
    dst = Path(args.target_file)
    dst_rel = dst.relative_to(get_repo_path(config.config_filename))
    cfg["operations"][dst_rel] = { system: unexpand(src) }
    config.save_config(cfg)

    return 0


command = StoreCommand()
