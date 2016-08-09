#!/usr/bin/env python

import os

CLONE_DIR = os.getenv('TRAVIS_BUILD_DIR'):

def projectpaths(directory):
	files = []

	for path in os.listdir(directory):
		if os.path.isdir(path):
			files += projectpaths(path)
		else if os.path.isfile(path):
			files[os.path.realpath(path)]
	
	return files

x = projectpaths(CLONE_DIR)

print(x)
