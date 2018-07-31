
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
    return 0


command = LinkCommand()
