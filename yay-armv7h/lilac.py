#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'yay'}]
repo_depends = [('fakeroot-tcp-armv7h', 'fakeroot-tcp')]
build_prefix = 'extra-armv7h'
time_limit_hours = 3

def pre_build():
    aur_pre_build('yay')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
