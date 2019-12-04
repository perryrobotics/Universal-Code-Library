#!/usr/bin/python
import os, sys
from wallaby import *
from constants import *

LM = 3
RM = 0
    
def move(speed, ticks):
	cmpc(LM)
  cmpc(RM)
  mrp(LM, speed, ticks)
  mrp(RM, speed, ticks)
  bmc(LM)
            
def move_back(speed, ticks):
	cmpc(LM)
  cmpc(RM)
  mrp(LM, -speed, ticks)
  mrp(RM, -speed, ticks)
  bmc(LM)

def move_left(speed, ticks):
	cmpc(LM)
  cmpc(RM)
  mrp(LM, -speed, ticks)
  mrp(RM, speed, ticks)
  bmc(LM)

def move_right(speed, ticks):
	cmpc(LM)
  cmpc(RM)
  mrp(LM, speed, ticks)
  mrp(RM, -speed, ticks)
  bmc(LM)
