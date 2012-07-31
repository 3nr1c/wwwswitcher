#!/usr/bin/env python

import re
import os

def readConfFile(name):
	handler = open(name,'r+b')
	content = handler.read()

	apachePath = re.findall('APACHEPATH.\'([^\']*?)\'',content)[0]
	localRoot = re.findall('LOCALROOT.\'([^\']*?)\'',content)[0]
	usingXampp = re.findall('USINGXAMPP.\'([^\']*?)\'',content)[0]
	xamppPath = re.findall('XAMPPPATH.\'([^\']*?)\'',content)[0]

	conf = [apachePath,localRoot,usingXampp,xamppPath]

	return conf

def openHttpdFile():
	config = readConfFile('switcher.conf')

	path = config[0]
	name = path+'conf\httpd.conf'

	hdlr = open(name, 'r', 1)
	return hdlr.read()

def changeFolder(newfolder):
	config = readConfFile('switcher.conf')

	newpath = config[1].replace('\\','/')+newfolder
	newstr = '<Directory "'+newpath+'">'
	newstr2 = 'DocumentRoot "'+newpath+'"'
	
	httpdContent = openHttpdFile()

	newHttpd = re.sub('<Directory (".*?")>',newstr,httpdContent,1)
	newHttpd = re.sub('DocumentRoot (".*?")',newstr2,newHttpd,1)

	return newHttpd

def saveChanges(newtext):
	config = readConfFile('switcher.conf')

	path = config[0]+'conf\httpd.conf'

	file(path,'w').write(newtext)

def apacheRestart():
	config = readConfFile('switcher.conf')

	os.system(config[0]+'bin\httpd.exe -k restart')

	#if config[2]:
	#	os.system(config[3]+'apache_stop.bat')
	#	os.system(config[3]+'apache_start.bat')