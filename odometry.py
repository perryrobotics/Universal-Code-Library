#!/usr/bin/python
import os, sys
from wallaby import *
from math import *
LM = 0
RM = 3
m = math
pi = m.pi
#These need to be changed for your robot!
TICKS_PER_ROT = 1000
WHEEL_CIRC_MM =  100
TICKS_PER_MM = TICKS_PER_ROT/WHEEL_CIRC_MM
base = 200
#base - the distance between the 2 front wheels
circ_of_base = pi * base
mm_per_deg = circ_of_base / 360

def forward_mm(speed, dist):
    cmpc(LM)
    cmpc(RM)
    total_ticks= dist*TICKS_PER_MM
    mrp(LM, speed, total_ticks)
    mrp(RM, speed, total_ticks)
    bmd(RM)


def back_mm(speed, dist):
    cmpc(LM)
    cmpc(RM)
    total_ticks= dist*TICKS_PER_MM
    mrp(LM, -speed, total_ticks)
    mrp(RM, -speed, total_ticks)
    bmd(RM)
    
def left_mm(speed, dist):
    cmpc(LM)
    cmpc(RM)
    total_ticks= dist*TICKS_PER_MM
    mrp(RM, speed, total_ticks)
    bmd(RM)

def right_mm(speed, dist):
    cmpc(LM)
    cmpc(RM)
    total_ticks= dist*TICKS_PER_MM
    mrp(LM, speed, total_ticks)
    bmd(LM)
    
def left_deg(speed, deg):
    cmpc(LM)
    cmpc(RM)
    mm_to_go = deg * mm_per_deg
    temp = mm_to_go / 2
    mrp(LM, -speed, temp)
    mrp(RM, speed, temp)
    bmd(RM)

def right_deg(speed, deg):
    cmpc(LM)
    cmpc(RM)
    mm_to_go = deg * mm_per_deg
    temp = mm_to_go / 2
    mrp(LM, speed, temp)
    mrp(RM, -speed, temp) 
    bmd(RM)
