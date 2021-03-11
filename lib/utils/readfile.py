def readfile(path):
	""" read file """
	if path != None or path != "":
		return [line.strip() for line in open(path,'rb')]
	return