from lib.utils.colors import *
from lib.utils.unicode import *

def plus(string,flag="[+]"):
	print "{}{}{} {}{}{}".format(
		GREEN%(0),flag,RESET,
		WHITE%(0),ucode(string),RESET
		)

def less(string,flag="[-]"):
	print "{}{}{} {}{}{}".format(
		RED%(0),flag,RESET,
		WHITE%(0),ucode(string),RESET
		)

def warn(string,flag="[!]"):
	print "{}{}{} {}{}{}".format(
		RED%(0),flag,RESET,
		RED%(0),ucode(string),RESET
		)

def test(string,flag="[*]"):
	print "{}{}{} {}{}{}".format(
		BLUE%(0),flag,RESET,
		WHITE%(0),ucode(string),RESET
		)
def info(string,flag="[i]"):
	print "{}{}{} {}{}{}".format(
		YELLOW%(0),flag,RESET,
		WHITE%(0),ucode(string),RESET
		)

def more(string,flag="|"):
	print " {}{}{}  {}{}{}".format(
		WHITE%(0),flag,RESET,
		WHITE%(0),ucode(string),RESET
		)

def null():
	print ""