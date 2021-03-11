from urllib2 import HTTPError

class WebscannerUnboundLocalError(UnboundLocalError):
	pass

class WebscannerDataException(Exception):
	pass

class WebscannerNoneException(Exception):
	pass

class WebscannerInputException(Exception):
	pass

class WebscannerGenericException(Exception):
	pass

class WebscannerConnectionException(HTTPError):
	pass

class WebscannerKeyboardInterrupt(KeyboardInterrupt):
	pass