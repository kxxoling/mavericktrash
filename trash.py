#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: kxxoling

import os, sys

TRASH_PATH = '/System/Library/CoreServices/Dock.app/Contents/Resources'
FILES = ['trashempty.png',
         'trashempty@2x.png',
         'trashemptyreflection.png',
         'trashemptyreflection@2x.png',
         'trashfull.png',
         'trashfull@2x.png']


def replace_file(somefile, source=os.path.join(os.getcwd(), 'macpro/')):
    sh = 'sudo cp %s %s' % (os.path.join(source, somefile), os.path.join(TRASH_PATH, somefile))
    os.popen(sh)


def macpro_trash():
    for f in FILES:
        replace_file(f)
    os.popen('killall Dock')
    print 'Replce Maverick Trash Icons with MacPro icons successfully!'


def recovery():
    for f in FILES:
        replace_file(f, source=os.path.join(os.getcwd(), 'maverick/'))
    os.popen('killall Dock')
    print 'Recover Maverick Trash Icons successfully!'


if __name__ == '__main__':
    if len(sys.argv) == 1:
        macpro_trash()
    elif sys.argv[1] == '-r':
        recovery()
    print "If this don't work, try to empty your Trash or add something to Trash."