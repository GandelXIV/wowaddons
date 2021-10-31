#!/usr/bin/python3

import os
import shutil
import zipfile

DEST = "/home/filip/Games/world-of-warcraft/drive_c/Program Files (x86)/World of Warcraft/_retail_/Interface/AddOns"

iszip = lambda name: name[-4:] == ".zip"

total_tasks = len(os.listdir())


for i, fn in enumerate(os.listdir()):
    if iszip(fn):
        print("[{0}/{1}] Copying:    {2}".format(i + 1, total_tasks, fn))
        shutil.copy(fn, DEST)
        print("[{0}/{1}] Extracting: {2}".format(i + 1, total_tasks, fn))
        with zipfile.ZipFile(fn, 'r') as zip_ref:
            zip_ref.extractall(DEST) 
        print("[{0}/{1}] Removing:   {2}".format(i + 1, total_tasks, fn))
        os.remove(DEST + '/' + fn)

