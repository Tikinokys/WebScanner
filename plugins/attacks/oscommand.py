from re import search,I
from lib.utils.params import *
from lib.utils.printer import *
from lib.request.request import *
from lib.utils.payload import os

class oscommand(Request):
	""" OS Command Injection """
	get = "GET"
	post = "POST"
	def __init__(self,kwargs,url,data):
		Request.__init__(self,kwargs)
		self.url = url 
		self.data = data

	def run(self):
		""" Run """
		info('Checking OS Command Injection...')
		URL = None
		DATA = None
		PAYLOAD = None
		for payload in os():
			# post method
			if self.data:
				# data add payload
				rPayload = padd(self.url,payload,self.data)
				for data in rPayload.run():
					# send request
					req = self.Send(url=self.url,method=self.post,data=data)
					# search payload in req.content
					if search('{}'.format(payload.split('"')[1]),req.content):
						URL = req.url 
						DATA = data 
						PAYLOAD = payload
						break
			# get method
			else:
				# url query add payload
				urls = padd(self.url,payload,None)
				for url in urls.run():
						# send request 
						req = self.Send(url=url,method=self.get)
						# search payload in req.content
						if search('{}'.format(payload.split('"')[1]),req.content):
							URL = url
							PAYLOAD = payload
							break
				# if URL and PAYLOAD not empty 
				if URL and PAYLOAD:
					# print 
					if DATA != None:
						plus("A potential \"OS Command Injection\" was found at:")
						more("URL: {}".format(URL))
						more("POST DATA: {}".format(DATA))
						more("PAYLOAD: {}".format(PAYLOAD))
					elif DATA == None:
						plus("A potential \"OS Command Injection\" was found at:")
						more("URL: {}".format(URL))
						more("PAYLOAD: {}".format(PAYLOAD))
					# break
					break