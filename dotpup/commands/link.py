from .base import BaseCommand


class LinkCommand(BaseCommand):
  def __init__(self):
    super().__init__(
        name="link",
        desc="Creates a symlink from a repo file to a target location "
        "and records the operation in dotpup.json for autolinking.")
    self.parser.add_argument("repo_file")
    self.parser.add_argument("target_file")

  def run(self, args):
    from dotpup.utils import symlink, save_operation
    from pathlib import Path
    repo_file = Path(args.repo_file)
    target_file = Path(args.target_file)

    if target_file.is_dir():
      target_file = target_file / repo_file.name

    symlink(repo_file, target_file)
    save_operation(repo_file, target_file)

    return 0


command = LinkCommand()
