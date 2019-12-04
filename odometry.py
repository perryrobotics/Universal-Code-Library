LM = 0
RM = 3

#These need to be changed for your robot!
TICKS_PER_ROT = 1000
WHEEL_CIRC_MM =  100
TICKS_PER_MM = TICKS_PER_ROT/WHEEL_CIRC_MM

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
    mrp(LM, -speed, total_ticks)
    mrp(RM, speed, total_ticks)
    bmd(RM)

def right_mm(speed, dist):
    cmpc(LM)
    cmpc(RM)
    total_ticks= dist*TICKS_PER_MM
    mrp(LM, speed, total_ticks)
    mrp(RM, -speed, total_ticks)
    bmd(RM)
