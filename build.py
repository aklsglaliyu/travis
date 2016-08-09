#!/usr/bin/env python

import os

CLONE_DIR = os.getenv('TRAVIS_BUILD_DIR')

files = [f for f in os.listdir(CLONE_DIR) if os.path.isfile(f)]

print(files)
