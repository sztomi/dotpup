from pathlib import Path

from .base import BaseCommand
from dotpup.config import config_filename

import dotpup.output as output


class InitCommand(BaseCommand):
  def __init__(self):
    super().__init__(
      name="init",
      desc="Creates an empty config file, marking the current directory "
           "a dotpup repository.")

  def run(self, args):
    output.info("Initializing current directory.")
    if Path(config_filename).exists():
      output.error(f"{config_filename} already exists "
                    "in the current directory")
      return 1
    with open(config_filename, "w") as _:
      pass
    output.info("Done.")
    return 0


command = InitCommand()
