
########################################################################################################
########################################################################################################
########################################################################################################

### PACKAGES ###########################################################################################

import os
import smtplib
import sys

print("Python version: {0}".format(sys.version))

### IMPORTS ############################################################################################

from src.bottle import route, get, post, request, response, template, static_file, redirect, SimpleTemplate, url

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

# dir = "foo"
# if the directory doesn't exist, create it
# if not os.path.exists(dir):
#     os.makedirs(dir)

### SMTP ###############################################################################################

receivers = []

def smtpInit(mailTo='', mailFrom='root'):
    # this is called from the wrapper file
    # sets the sender and receiver for emails
    global receivers
    global sender

    receivers = [mailTo]
    sender = mailFrom

### STATIC ROUTING ########################################################################################

# CSS
@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    # print("IN STYLESHEETS():", filename)
    return static_file(filename, root='../static/css')

# JAVASCRIPT
@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    # print("IN JAVASCRIPTS():", filename)
    return static_file(filename, root='../static/js')

# IMAGES
@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    # print("IN IMAGES():", filename)
    return static_file(filename, root='../static/img')

# FONTS
@get('/fonts/<filename:re:.*\.(eot|ttf|woff|woff2|svg)>')
def fonts(filename):
    # print("IN FONTS():", filename)
    return static_file(filename, root='../static/fonts')

### COOKIE GETTERS/SETTERS #############################################################################

# def getCookie(request):
#     return request.get_cookie("foo") or ""
#
# def setCookie(response, value):
#     response.set_cookie("foo", value)


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
######################################### foo START #############################################
########################################################################################################

used_tokens = []

# comment
@get('/index')
def get_foo():

    # PyCharm false import error : it works
    from passlib.hash import sha256_crypt as sha256

    from time import strftime

    secret = ""
    try:
        f = open("../.secret")
        secret = f.read().strip()
        f.close()
    except IOError:
        return "Secret not found"

    # code
    time = strftime("%H:%M:%S")

    date_salt = strftime("%d%m%y")

    token = sha256.encrypt(date_salt + secret)

    msg = "Check if token decryption is valid"

    return template('index', time=time, msg=msg, token=token, records=[])

########################################################################################################
########################################################################################################

@post('/index')
def post_foo():

    from passlib.hash import sha256_crypt as sha256

    from time import strftime


    # code
    print("POST RECEIVED")

    token = request.forms.get('token')

    secret = ""
    try:
        f = open("../.secret")
        secret = f.read().strip()
        f.close()
    except IOError:
        return "Secret not found"

    time = strftime("%H:%M:%S")

    date_salt = strftime("%d%m%y")

    verified = False

    msg = "Token invalid"

    records = []

    if token in used_tokens:
        msg = "Token already used"
    else:
        try:
            verified = sha256.verify(date_salt + secret, token)
        except ValueError:
            msg = "Token malformed"

        if verified:
            msg = "Token verified"
            used_tokens.append(token)
            records = ['foo', 'bar', 'baz']

    return template('index', time=time, msg=msg, token=token, records=records)

########################################################################################################
######################################### foo END ###############################################
########################################################################################################





########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################