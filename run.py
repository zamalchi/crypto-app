#!/usr/bin/python

import argparse

from src.bottle import run

from src.main import *

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', help = "Port number", action="store", dest="p", required = True)

parser.add_argument('-s', help = "Sender address", action="store", dest="s", required = False)
parser.add_argument('-m', help = "Receiver address", action="store", dest="m", required = False)

# parser.add_argument('-d', help = "Dev mode", action="store", dest="d", required = False) # True|1 / False|0

args = parser.parse_args()

port = args.p
mailFrom = args.s
mailTo = args.m
# dev = args.d

smtpInit(mailTo, mailFrom)

# if dev == "True":
    # reloader: restart on module file change
    # run(reloader=True, host='localhost', port=port, debug=True)
# else:

run(host='172.16.1.254', port=port, debug=True)
