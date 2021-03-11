from time import strftime
from random import randint,choice
from string import uppercase,lowercase

def r_time():
	""" random numbers """
	return randint(0,int(strftime('%y%m%d')))

def r_string(n):
	""" random strings """
	return "".join([choice(uppercase+lowercase) for _ in xrange(0,int(n))])