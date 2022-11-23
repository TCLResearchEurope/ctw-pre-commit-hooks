#!/usr/bin/env python
import os
import sys


HOOK_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    cfg = os.path.join(HOOK_DIR, 'general-hooks.yaml')
    cmd = ['pre-commit', 'run', '--config', cfg, '--files'] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
