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

#line average
def line_average(port,times):
	line = []
	for x in range(times):
		line.append(analog(port))
	for x in range(times):
		line[0] = line[0]+line.pop(1)
	line_average = line[0]/times
	return line_average

def line_median(port, times):
	med = []
	if times%2 == 1:
 		times = times+1
	for x in range(times)
		med.append(analog(port))
	med.sort()
	median = times/2
	return med[median]

def line_average_median(port,times):
	median = []
	for x in times:
		line = []
		for x in range(times):
			line.append(analog(port))
		for x in range(times):
			line[0] = line[0]+line.pop(1)
		line_average = line[0]/times
		median.append(line_average)
	median.sort()
	if times%2 == 1:
		times = times +1
	med = times/2
	return median[med]
