#!/usr/bin/env sh

apt-get update -qq
apt-get upgrade -qq
apt-get install python python-pip
pip install requests
