# sonargame.py
# in this game you have find 3 sinked treasures using 20 sonar
# using cartesian coordinate sysytem

import random, sys, math, pygame

def drawWave ():
	wave = ''
	waveList = ['.','`','~','~']
	for i in range (50):
		wave = wave + random.choice(waveList)
	
	return wave


def drawsea ():
	print ()
	for i in range (50):
		if ((i % 10) == 0): 
			print (int (i / 10), end = '')
		else:
			print (' ', end = '')
	print ()
	for i in range (50):
		print (i % 10, end = '')
	print ()
	for i in range (20):
		print (drawWave() + ' ' + str(i))
	

drawsea () 
