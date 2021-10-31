#!/usr/bin/python3

import os
import sys
import shutil
import zipfile


iszip = lambda name: name[-4:] == ".zip"

def rf(name):
    with open(name, 'r') as f:
        return f.read()

DEST = rf("destination.cfg").strip()

def install(files, dest):
    total_tasks = len(list(filter(lambda x: iszip(x), files)))
    i = 0
    for fn in files:
        if iszip(fn):
            i += 1
            print("[{0}/{1}] Copying:    {2}".format(i , total_tasks, fn))
            shutil.copy(fn, dest)
            print("[{0}/{1}] Extracting: {2}".format(i , total_tasks, fn))
            with zipfile.ZipFile(fn, 'r') as zip_ref:
                zip_ref.extractall(dest) 
            print("[{0}/{1}] Removing:   {2}".format(i , total_tasks, fn))
            os.remove(dest + '/' + fn)

def main():
    install(os.listdir(), DEST)

if __name__ == "__main__":
    main()

