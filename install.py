#!/usr/local/bin/python
__author__ = 'dannwebster'

import os
from os import symlink
from os.path import join, exists, relpath

contrib_home_path="/Users/dwebster/Documents/RPGs/Gurps-Character-Sheet-contrib-"
gcs_home_path="/Applications/GURPScs"

contrib_lib_path=join(contrib_home_path, "Library")
gcs_lib_path=join(gcs_home_path, "Library")


contrib_dirs=[]
for root, subdirs, files in os.walk(contrib_lib_path):
    rel = relpath(root, contrib_lib_path)
    for subdir in subdirs:
        contrib_dirs.append(join(rel, subdir))

new_dirs=[ f for f in contrib_dirs if not exists(join(gcs_lib_path, f)) ]
for new_dir in new_dirs:
    real_dir = join(contrib_lib_path, new_dir)
    sym_link = join(gcs_lib_path, new_dir)
    if (not exists(sym_link)):
        print("Linking " + sym_link + " to " + real_dir)
        symlink(real_dir, sym_link)
    else:
        print("Linking " + sym_link + " already exists ")

