import sys
import getopt
# -- lib
from lib.utils.printer import *
from lib.utils.usage import *
from lib.utils.check import *
from lib.utils.settings import *
from lib.request.ragent import *
from lib.utils.exception import *
# -- modules
from lib.handler.attacks import *

class webscanner(object):
	usage = usage()
	def main(self):
		kwargs = ARGS
		# verbose default == False
		verbose = False
		scan = "1"
		if len(sys.argv) < 2:
			# True == exit
			self.usage.basic(True)
		try:
			opts,args = getopt.getopt(ARGV[1:],CHAR,LIST_NAME)
		except getopt.GetoptError,e:
			# True == exit
			self.usage.basic(True)
		self.usage.banner()
		# process args 
		for opt,arg in opts:
			if opt in ('-u','--url'):url = CUrl(arg) 
			if opt in ('-s','--scan'):scan = CScan(arg) 
			if opt in ('-V','--version'):version = Version()
			if opt in ('-hh','--help'):self.usage.basic(True)
		# starting 
		parse = SplitURL(url)
		try:
			PTIME(url)
			if scan == 1:
				Attacks(kwargs,url,kwargs['data'])
		except WebscannerUnboundLocalError,e:
			pass

if __name__ == "__main__":
	try:
		webscanner().main()
	except KeyboardInterrupt,e: 
		exit(warn('Exiting... :('))