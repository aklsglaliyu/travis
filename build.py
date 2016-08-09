#!/usr/bin/env python

import os

print(os.getenv('TRAVIS_BUILD_DIR'))
print(os.getenv('TRAVIS_BUILD_ID'))
print(os.getenv('TRAVIS_TAG'))
print(os.getenv('TRAVIS_REPO_SLUG'))
print(os.getenv('TRAVIS_JOB_ID'))
print(os.getenv('TRAVIS_JOB_NUMBER'))
