from sys import argv
from time import strftime
from lib.request.ragent import *
from lib.utils.printer import *


# tool name
NAME = argv[0]

# tool version
VERSION = "v1.0.1"

# author
AUTHOR = "Tikinokys"

# description
DESCRIPTION = "WebScanner"

# name + description + version
NVD = (NAME.split('.')[0]).title()+": "+DESCRIPTION+" - "+VERSION

# max threads
MAX = 5

# args
CHAR = "u:s:H:d:m:h:R:a:A:c:p:P:t:n:v=:V=:r=:b=:"

LIST_NAME = [
    "url=",
    "scan=",
    "version",
    "help"
]

# argv
ARGV = argv
# dict args
ARGS = {
    'data': None,
    'method': 'GET'
}

# time
TIME = strftime('%d/%m/%Y at %H:%M:%S')
TNOW = strftime('%H:%M:%S')


# print version
def Version():
    print "\n{}".format(NVD)
    print "Author: {}\n".format(AUTHOR)
    exit()


# print time and url
def PTIME(url):
    plus("URL: {}".format(url))
    plus("Starting: {}".format(TIME))
    null()
