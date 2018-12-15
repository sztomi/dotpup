## dotpup manages dotfiles across platforms

This is very minimalistic and intended for my own usage, but maybe others
will find it useful. dotpup doesn't care about the synchronization of files,
it's up to you. You may use git, rsync, dropbox, nextcloud etc.

## Installation

```
$ pip3 install dotpup
```

Python 3.6+ is required.

## Usage

dotpup has three commands. All of them require setting DOTPUP_HOME. Typically,
you will want to have a dotfiles directory somewhere (I have `$HOME/dotfiles`).

You can start with an empty directory.

### dpup store

```
$ dpup store <some dotfile>
```

This moves the dotfile into `$DOTPUP_HOME`, symlinks it back to the original
location and records the transaction for future automated replication (see
`dpup update`)

This is my current dotpup.json:

```
{
  "operations": {
    "Darwin": {
      ".config/nvim/init.vim": "$HOME/.config/nvim/init.vim",
      ".gitconfig": "$HOME/.gitconfig",
      ".gitignore_global": "$HOME/.gitignore_global",
      ".tmux.conf": "$HOME/.tmux.conf",
      ".zsh_aliases": "$HOME/.zsh_aliases",
      ".zshrc": "$HOME/.zshrc"
    },
    "Linux": {
      ".config/nvim/init.vim": "$HOME/.config/nvim/init.vim",
      ".gitconfig": "$HOME/.gitconfig",
      ".gitignore_global": "$HOME/.gitignore_global",
      ".hosts": "$HOME/.hosts",
      ".ssh/config": "$HOME/.ssh/config",
      ".tmux.conf": "$HOME/.tmux.conf",
      ".zsh_aliases": "$HOME/.zsh_aliases",
      ".zshrc": "$HOME/.zshrc"
    }
  }
}
```

The reason for having per-platform entries is that the paths are not always the
same. For example, vscode (which I'm yet to add) uses different paths on Linux
and macOS.

### dpup link

```
$ dpup link <some stored dotfile> <target location>
```

This creates a symlink to a stored dotfile and records the operation. This is
typically useful when reusing dotfiles on a new platform.

### dpup update

```
$ dpup update
```

This performs the operations for the current platform or (optionally) for a
different platform. This is useful when you are setting up on a new machine.
