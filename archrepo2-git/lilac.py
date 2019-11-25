#!/bin/python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'github': 'archlinuxcn/repo', 'path': 'archlinuxcn/archrepo2-git/PKGBUILD'}, {'github': 'lilydjwg/archrepo2'}]
build_prefix = 'extra-x86_64'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxcn/repo', 'archlinuxcn/archrepo2-git/PKGBUILD'])
    run_cmd(['rm', 'lilac.yaml'])
    run_cmd(['git', 'restore', 'lilac.py'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)