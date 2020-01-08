#!/usr/bin/python
import os, sys
from wallaby import *
RM=3
LM=0
Touch_port=1
Line_port=2
Thresh = 2500

def drive_to_black(speed):
	mav(RM, speed)
	mav(LM, speed)
	while analog(Line_port) < Thresh:
		pass
	ao()
            
def drive_to_white(speed):
	mav(RM, speed)
	mav(LM, speed)
	while analog(Line_port) > Thresh:
		pass
	ao()    
   
def right_to_black(speed):
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while analog(Line_port) < Thresh:
		pass
	ao()   
            
def left_to_black(speed):
	mav(Lmotor, -speed)
	mav(Rmotor, speed)
	while analog(Line_port) < Thresh:
		pass
	ao()  
   
def right_to_white(speed):
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while analog(Line_port) > Thresh:
		pass
	ao()  
  
def left_to_white(speed):
	mav(Lmotor, -speed)
	mav(Rmotor, speed)
	while analog(Line_port) > Thresh:
		pass
	ao()  

def line_average():
	line = []
	for x in range(15):
		line.append(analog(line_port))
	for x in range(15):
		line[0] = line[0]+line.pop(1)
	final = line[0]/15
