wwwswitcher - Change your Apache server folder easily.
v0.1 by Enric Florit
Enjoy! Feedback is welcome: efz1005[at]gmail[dot]com

Alpha version - use at your own risk
Only tested on Windows 7

Python 2.7+ is needed
________________________


IMPORTANT!!!!!
BEFORE STARTING, configure correctly the 'switcher.conf' file!
APACHEPATH = the folder where you have the Apache files
LOCALROOT = the folder where you have the diferent server folders

Example: the localRoot could be c:\www, and into it you could have 'ww1' and 'ww2'
folders. This is useful for testing two webs at once.

________________________

To run it execute 'consoleversion.py'.

There are only two commands, 'changeto' and 'exit'
Use: 'changeto folder', example 'changeto ww1'

________________________
Note: if you're using XAMPP, you'll have to restart Apache manually 
after changing the server folder