#!/usr/bin/python

import argparse

from src.bottle import run

from src.main import *

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', help = "Port number", action="store", dest="p", required = True)

args = parser.parse_args()

port = args.p

run(host='172.16.1.254', port=port, debug=True)
