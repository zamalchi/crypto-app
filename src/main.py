
### PACKAGES ###########################################################################################

import os
import sys

### IMPORTS ############################################################################################

from src.bottle import \
    get, post, redirect, \
    request, response,\
    template, static_file,\
    SimpleTemplate, url

from time import strftime

from src.crypto import *

from classes.Record import Record, RecordMalformedException

from config.dirs import ROOT_DIR

### APACHE #############################################################################################

os.chdir(os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(__file__))

### RUNNING AS MAIN ####################################################################################

if __name__ == "__main__":
    print("Run app through wrapper.")
    print("Exiting...")
    exit()

### FOR CSS READING IN TEMPLATES #######################################################################

SimpleTemplate.defaults["url"] = url

### DIRECTORY ##########################################################################################

# directory for saving hours information - set in Record.py, so this is redundant
Record.hoursDir = os.path.join(ROOT_DIR, "hours")

# if the directory doesn't exist, create it
if not os.path.exists(Record.hoursDir):
    os.makedirs(Record.hoursDir)

### STATIC ROUTING ########################################################################################

# CSS
@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static/css'))

# JAVASCRIPT
@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static/js'))

# IMAGES
@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static/img'))

# FONTS
@get('/fonts/<filename:re:.*\.(eot|ttf|woff|woff2|svg)>')
def fonts(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static/fonts'))

### COOKIE GETTERS/SETTERS #############################################################################

# def getCookie(request):
#     return request.get_cookie("foo") or ""
#
# def setCookie(response, value):
#     response.set_cookie("foo", value)


### HELPER FUNCTIONS ###################################################################################


########################################################################################################
########################################################################################################
########################################################################################################

#
#
#
# ^^^ FUNCTIONS, SETTINGS ^^^
#
# vvv ROUTES vvv
#
#
#

########################################################################################################
########################################################################################################
########################################################################################################

@get('/receive')
def receive_records():

    name = request.query['n']

    date = request.query['d']

    b64 = request.query['r']

    decrypted = filter(None, getDecodedString(b64).split("\n"))

    validated = False
    try:
        # check if each record is a valid record
        for r in decrypted:
           Record(r)
        # if all were successful
        validated = True

    except RecordMalformedException:
        validated = False

    string = ''.join(decrypted)

    # if unable to decrypt, name will not show up in the string
    if name not in string or not validated:
        return "<h2>Couldn't decrypt records</h2>"

    else:
        filename = os.path.join(Record.hoursDir, date + "-" + name)

        f = open(filename, 'w')

        for r in decrypted:
            f.write(r + "\n")

        f.close()

        return "<h2>Saved to {0}-{1}</h2>".format(date, name)

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################