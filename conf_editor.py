# encoding: utf-8

import sys
import argparse

from workflow import ICON_SETTINGS
from workflow import (Workflow, ICON_WARNING)
import os


userpath = lambda p: os.path.expanduser(p)

PROGRAMS = {
    'ssh': userpath('~/.ssh/config'),
    'nginx': '/usr/local/etc/nginx/nginx.conf',
    'zsh': userpath('~/.zshrc'),
    'hosts': '/etc/hosts',
    'git': userpath('~/.gitconfig'),
    'vim': userpath('~/.vimrc'),
    'tumx': userpath('~/.tmux.conf'),
    'mackup': userpath('~/.mackup.cfg'),
    'shadowsocks': userpath('~/.ShadowsocksX/gfwlist.js'),
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
        wf.add_item(title=program,
                    subtitle=PROGRAMS[program],
                    arg=PROGRAMS[program],
                    valid=True,
                    icon=ICON_SETTINGS)

    wf.send_feedback()
    return 0


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
