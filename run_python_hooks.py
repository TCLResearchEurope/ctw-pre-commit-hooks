#!/usr/bin/env python
import os
import sys
import shutil


HOOK_DIR = os.path.dirname(os.path.realpath(__file__))


def copy_config_file(file_name: str) -> None:
    project_dir = os.getcwd()
    shutil.copyfile(os.path.join(HOOK_DIR, file_name), os.path.join(project_dir, file_name))


def main():
    copy_config_file(".flake8")
    copy_config_file(".isort.cfg")
    copy_config_file(".black.toml")
    copy_config_file("requirements-pre-commit-hooks.txt")
    cfg = os.path.join(HOOK_DIR, 'python-hooks.yaml')
    cmd = ['pre-commit', 'run', '--config', cfg, '--files'] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
