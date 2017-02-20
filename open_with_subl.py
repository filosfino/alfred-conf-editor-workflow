# encoding: utf-8

import os
import sys
import argparse

from workflow import ICON_SETTINGS
from workflow import (Workflow, ICON_WARNING)


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='paths', nargs='*', default=None)
    args = parser.parse_args(wf.args)
    paths = ' '.join(args.paths)
    os.system('/usr/local/bin/subl -an %s' % paths)
    return 0


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
