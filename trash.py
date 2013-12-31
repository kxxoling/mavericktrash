#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: kxxoling

import os

TRASH_PATH = '/System/Library/CoreServices/Dock.app/Contents/Resources'
FILES = ['trashempty.png',
         'trashempty@2x.png',
         'trashemptyreflection.png',
         'trashemptyreflection@2x.png',
         'trashfull.png',
         'trashfull@2x.png']


def replace_file(somefile, source=os.path.join(os.getcwd(), 'macpro/')):
    sh = 'sudo cp %s %s' % (os.path.join(source, f), os.path.join(TRASH_PATH, somefile))
    os.popen(sh)

if __name__ == '__main__':
    for f in FILES:
        replace_file(f)
    os.popen('killall Dock')
