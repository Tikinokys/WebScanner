from lib.utils.colors import * 
from lib.utils.settings import NAME,VERSION

class usage:
	""" docstring for usage """
	def banner(self):
		mx = "_"*70
		print mx
		print "%s ________ _______ __      _______                   %s"%(YELLOW%(0),RESET)
		print "%s|  |  |  |   ____|  |____|     __|.----.---.-.-----.-----.-----.-----.%s"%(YELLOW%(0),RESET)
		print "%s|  |  |  |   ____|   __  |__     ||  __|  _  |     |     |  ___|   __|%s"%(YELLOW%(0),RESET)
		print "%s|________|_______|_______|_______||____|___._|__|__|__|__|_____|___|%s"%(YELLOW%(0),RESET)
		print "                                                                %s%s%s"%(YELLOW%(1),VERSION,RESET)
		print mx+"\n"

	def basic(self,_exit_=True):
		self.banner() 
		print "Usage: %s [options]\n"%NAME
		print "\t-u --url\tTarget URL (e.g: http://www.site.com)"
		print "\t-s --scan\tScan options:\n"
		print "\t\t1 :\tAttacks (sql,ldap injection,...)"
		print "\t-V --version\tShow tool version"
		print "\t-hh --help\tShow this help and exit\n"
		if _exit_: exit(0)