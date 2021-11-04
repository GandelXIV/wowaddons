#!/usr/bin/python3

import os
import sys
import shutil
import zipfile


iszip = lambda name: name[-4:] == ".zip"

def rf(name):
    with open(name, 'r') as f:
        return f.read()

def log(msg):
    if LOGS:
        print(msg)

DEST = rf("destination.cfg").strip()
ADDONS = "addons/"
LOGS = True

def install(files, dest):
    total_tasks = len(list(filter(lambda x: iszip(x), files)))
    i = 0
    for fn in files:
        i += 1
        log("[{0}/{1}] Copying:    {2}".format(i , total_tasks, fn))
        shutil.copy(ADDONS + fn, dest)
        log("[{0}/{1}] Extracting: {2}".format(i , total_tasks, fn))
        with zipfile.ZipFile(ADDONS + fn, 'r') as zip_ref:
            zip_ref.extractall(dest) 
        log("[{0}/{1}] Removing:   {2}".format(i , total_tasks, fn))
        os.remove(dest + '/' + fn)

def main():
    log("Starting...")
    install(os.listdir(ADDONS), DEST)
    log("Done!")

if __name__ == "__main__":
    main()

