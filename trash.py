#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: kxxoling

import os
import sys
import shutil

TRASH_PATH = '/System/Library/CoreServices/Dock.app/Contents/Resources'
FILES = ['trashempty.png',
         'trashempty@2x.png',
         'trashemptyreflection.png',
         'trashemptyreflection@2x.png',
         'trashfull.png',
         'trashfull@2x.png']

def replace_file(src, dst=TRASH_PATH, path='macpro/'):
    path = os.path.join(os.getcwd(), path)
    src = os.path.join(path, src)
    try:
        shutil.copy(src, dst)
    except IOError:
        print 'No file named %s, passed.' % (src)


def macpro_trash():
    for f in FILES:
        replace_file(f)
    print '🍺 Replce Maverick Trash Icons with MacPro icons successfully!'


def recovery():
    for f in FILES:
        replace_file(f, path='maverick/')
    print '🍺 Recover Maverick Trash Icons successfully!'


if __name__ == '__main__':
    if len(sys.argv) == 1:
        macpro_trash()
    elif sys.argv[1] == '-r':
        recovery()
    print 'Please manually run "killall Dock".'
    print "If this don't work, try to empty your Trash or add something to Trash."