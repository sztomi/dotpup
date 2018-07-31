import os

from setuptools import setup, find_packages

setup(
  name="dotpup",
  version=os.environ.get("DOTPUP_VERSION", "1.0.9999"),
  packages=find_packages(),
  license="MIT",
  long_description=open("README.md").read(),
  entry_points = {
    "console_scripts": ["dpup=dotpup.cli:cli"],
  }
)
