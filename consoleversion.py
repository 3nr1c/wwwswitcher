#!/usr/bin/env python

from functions import readConfFile
from functions import openHttpdFile
from functions import changeFolder
from functions import saveChanges
from functions import apacheRestart

version = '0.1'

print 'wwwswitcher'
print 'v'+version

while(True):
	inpt = raw_input('>')

	if inpt[0:8] == 'changeto':
		newFolder = inpt[9:].strip()
		newStr = changeFolder(newFolder)
		saveChanges(newStr)
		apacheRestart()
	if inpt == 'exit':
		exit()