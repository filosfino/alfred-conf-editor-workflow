# encoding: utf-8

import os
import sys
import argparse
import pipes

from workflow import ICON_SETTINGS
from workflow import (Workflow, ICON_WARNING)


def expand_user_path(p):
    return os.path.expanduser(p)


PROGRAMS = {
    'supervisor': [
        '/usr/local/etc/supervisor.d/',
        '/usr/local/etc/supervisord.conf',
    ],
    'ranger': [
        '~/.config/ranger/rc.conf',
        '~/.config/ranger',
    ],
    'cargo': [
        '~/.cargo/config',
    ],
    'ssh': [
        '~/.ssh/config',
        '~/.ssh',
    ],
    'starship': [
        '~/.config/starship.toml',
    ],
    'rime': [
        '~/Library/Rime',
        '~/Library/Rime/squirrel.custom.yaml',
        '~/Library/Rime/luna_pinyin_simp.custom.yaml',
        '~/Library/Rime/luna_pinyin.custom.yaml',
        '~/Library/Rime/installation.yaml',
        '~/Library/Rime/default.custom.yaml',
        '~/Dropbox/Sync/Rime',
    ],
    'nginx': [
        '/usr/local/etc/nginx/nginx.conf',
        '/usr/local/etc/nginx',
    ],
    'zsh': '~/.zshrc',
    'hosts': '/etc/hosts',
    'git': [
        '~/.gitconfig',
        '~/.gitignore',
    ],
    'vim': [
        '~/.vimrc',
        '~/.vim',
    ],
    'nvim': [
        '~/.config/nvim/init.vim',
        '~/.config/nvim',
    ],
    'tmux': '~/.tmux.conf',
    'mackup': [
        '~/.mackup.cfg',
        '~/.mackup',
    ],
    'shadowsocks': [
        '~/.ShadowsocksX-NG/user-rule.txt',
        '~/.ShadowsocksX-NG',
    ],
    'v2ray': [
        '~/Dropbox/Sync/v2ray/client/config.json',
        '~/Dropbox/Sync/v2ray/server/config.json',
    ],
    'fish': [
        '~/.config/fish/config.fish',
        '~/.config/fish',
        '~/.config/fish/fishfile',
    ],
    'conf_editor': [
        '~/Dropbox/Sync/Alfred.alfredpreferences/workflows/user.workflow.E39B5FB1-DC6B-439A-9448-7184DB0ECA3C/conf_editor.py',
        '~/Dropbox/Sync/Alfred.alfredpreferences/workflows/user.workflow.E39B5FB1-DC6B-439A-9448-7184DB0ECA3C',
    ],
    'blog': [
        "~/projects/blog",
    ],
    'ansible': [
        '~/.ansible.cfg',
        '~/.ansible',
    ],
    'projects': [
        '~/projects',
    ],
    'virtualenv': [
        '~/.virtualenvs',
    ],
    'mysql': [
        '~/.my.cnf',
    ],
    'scripts': [
        '~/Dropbox/scripts/brew.sh',
        '~/Dropbox/scripts',
    ],
    'ipython': [
        '~/.ipython/profile_default/ipython_config.py',
        '~/.ipython/profile_default',
        '~/.ipython',
    ],
    'jupyter': [
        '~/.jupyter',
        '~/.jupyter/jupyter_notebook_config.py',
    ],
    'npm': [
        '~/.npmrc',
    ],
    'yarn': [
        '~/.yarnrc',
    ],
    'rclone': [
        '~/.config/rclone/rclone.conf',
    ],
    'alacritty': [
        '~/.config/alacritty/alacritty.yml',
    ],
}

PROGRAMS = {key: list(map(expand_user_path, PROGRAMS[key])) for key in PROGRAMS}


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='program', nargs='?', default=None)
    args = parser.parse_args(wf.args)

    user_program = args.program

    if not user_program:
        wf.add_item('Enter program name to continue', icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    programs = wf.filter(user_program, PROGRAMS)

    if not programs:
        wf.add_item('No program found', icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    for program in programs:
        if isinstance(PROGRAMS[program], (list, tuple)):
            paths = [pipes.quote(path) for path in PROGRAMS[program]]
            paths = ' '.join(paths)
        else:
            paths = pipes.quote(PROGRAMS[program])

        wf.add_item(title=program,
                    subtitle=paths,
                    arg=paths,
                    valid=True,
                    icon=ICON_SETTINGS)

    wf.send_feedback()
    return 0


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
