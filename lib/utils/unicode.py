def ucode(string):
	if isinstance(string,unicode):
		return string.encode('utf-8')
	return string