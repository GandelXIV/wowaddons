#!/usr/bin/python3

import os
import shutil
import zipfile

DEST = "/home/filip/Games/world-of-warcraft/drive_c/Program Files (x86)/World of Warcraft/_retail_/Interface/AddOns"

iszip = lambda name: name[-4:] == ".zip"

for fn in os.listdir():
    if iszip(fn):
        print("Copying", fn)
        shutil.copy(fn, DEST)

for fn in os.listdir(DEST):
    if iszip(fn):
        print("Extracting", fn)
        with zipfile.ZipFile(fn, 'r') as zip_ref:
            zip_ref.extractall(DEST) 

for fn in os.listdir(DEST):
    if iszip(fn):
        print("Removing", fn)
        os.remove(DEST + '/' + fn)
