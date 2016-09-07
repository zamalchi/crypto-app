#!/usr/bin/python

import argparse

from src.bottle import run

from src.main import *

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-h', help = "Host address", action="store", dest="h", required = True)
parser.add_argument('-p', help = "Port number", action="store", dest="p", required = True)

args = parser.parse_args()

port = args.p
host = args.h

run(host=host, port=port, debug=True)
