from os import path
from random import randint
from lib.utils.readfile import *

def ragent():
	"""random agent"""
	user_agents = ()
	realpath = path.join(path.realpath(__file__).split('lib')[0],'lib/db/')
	realpath += "useragent.webscanner"
	for _ in readfile(realpath):
		user_agents += (_,)
	return user_agents[randint(0,len(user_agents)-1)]