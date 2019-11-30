#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'annie'}]
build_prefix = 'extra-armv7h'

def pre_build():
    aur_pre_build('annie')
    add_arch(['armv7h'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)