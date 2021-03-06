import os
import sys
from lib.utils.dirs import *
from lib.utils.printer import *
from importlib import import_module

path = os.path.join(os.path.abspath('.').split('lib')[0],'plugins/attacks/')

def Attacks(kwargs,url,data):
	info('Starting attacks module...')
	for file in dirs(path):
		file = file.split('.py')[0]
		__import__('plugins.attacks.%s'%(file))
		module = sys.modules['plugins.attacks.%s'%(file)]
		module = module.__dict__[file]
		module(kwargs,url,data).run()