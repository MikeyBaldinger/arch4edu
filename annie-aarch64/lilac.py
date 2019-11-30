#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'annie'}]
build_prefix = 'extra-aarch64'

def pre_build():
    aur_pre_build('annie')
    add_arch(['aarch64'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)