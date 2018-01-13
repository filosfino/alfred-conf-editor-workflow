# encoding: utf-8

import os
import sys
import argparse
import pipes

from workflow import ICON_SETTINGS
from workflow import (Workflow, ICON_WARNING)


userpath = lambda p: os.path.expanduser(p)

PROGRAMS = {
    'supervisor': [
        '/usr/local/etc/supervisor.d/',
        '/usr/local/etc/supervisord.conf',
    ],
    'ssh': [
        userpath('~/.ssh/config'),
        userpath('~/.ssh'),
    ],
    'nginx': [
        '/usr/local/etc/nginx/nginx.conf',
        '/usr/local/etc/nginx',
        '/usr/local/Cellar/nginx-full/1.10.3',
    ],
    'zsh': userpath('~/.zshrc'),
    'hosts': '/etc/hosts',
    'git': userpath('~/.gitconfig'),
    'vim': userpath('~/.vimrc'),
    'tmux': userpath('~/.tmux.conf'),
    'mackup': [
        userpath('~/.mackup.cfg'),
        userpath('~/.mackup'),
    ],
    'shadowsocks': userpath('~/.ShadowsocksX/gfwlist.js'),
    'fish': [
        userpath('~/.config/fish/config.fish'),
        userpath('~/.config/fish'),
    ],
    'fisherman': [
        userpath('~/.config/fish/fishfile'),
        userpath('~/.config/fisherman'),
    ],
    'conf_editor': [
        userpath('~/Library/Mobile Documents/com~apple~CloudDocs/Mackup/.config/Alfred/Alfred.alfredpreferences/workflows/user.workflow.E39B5FB1-DC6B-439A-9448-7184DB0ECA3C/conf_editor.py'),
        userpath('~/Library/Mobile Documents/com~apple~CloudDocs/Mackup/.config/Alfred/Alfred.alfredpreferences/workflows/user.workflow.E39B5FB1-DC6B-439A-9448-7184DB0ECA3C'),
    ],
    'ansible': [
        userpath('~/.ansible.cfg'),
        userpath('~/.ansible'),
    ],
    'projects': [
        userpath('~/projects'),
        userpath('~/documents/projects'),
    ],
    'virtualenv': [
        userpath('~/.virtualenvs'),
    ],
    'mysql': [
        userpath('~/.my.cnf'),
    ],
    'blog': [
        userpath('~/documents/projects/filosfino/_config.yml'),
        userpath('~/documents/projects/filosfino/themes/apollo/_config.yml'),
        userpath('~/documents/projects/filosfino/'),
        userpath('~/documents/projects/filosfino/source/_posts/'),
    ],
    'scripts': [
        userpath('~/Documents/Scripts/brew.sh'),
        userpath('~/Documents/Scripts'),
    ],
    'ipython': [
        userpath('~/.ipython/profile_default/ipython_config.py'),
        userpath('~/.ipython/profile_default'),
    ],
    'jupyter': [
        userpath('~/.jupyter'),
        userpath('~/.jupyter/jupyter_notebook_config.py'),
    ],
}


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
