#!/usr/bin/env python

import nxt.locator
import time
from nxt.motor import *
from nxt.sensor import *

b = nxt.locator.find_one_brick()

def forward():
        if Ultrasonic(b, PORT_4).get_sample() >= 10:
                print Ultrasonic(b, PORT_4).get_sample()
                sm = SynchronizedMotors(m_right, m_left, 0)
                sm.turn(127, 360)
        else:
                stuck()
        
def backward():
        sm = SynchronizedMotors(m_right, m_left, 0)
        sm.turn(-127, 360)
        
def right():
        sm = SynchronizedMotors(m_right, m_left, 127)
        sm.turn(127, 180)
        
def left():
        sm = SynchronizedMotors(m_left, m_right, 127)
        sm.turn(127, 180)
        
def stuck():
        sm = SynchronizedMotors(m_right, m_left, 0)
        sm.turn(-127, 1000)

m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
m_grab = Motor(b, PORT_A)
