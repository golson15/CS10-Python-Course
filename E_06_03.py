#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Episteme 06_03 Flood Animation

Created on Mon Oct 14 21:35:58 2019

@author: Grace Olson and Jack Chiplin
"""

#this was a sad attempt

def floodAnimation(heights) :
    # Create the window with a good size
    w = GraphicsWindow(500, 500)
    canvas = w.canvas()
    w.setTitle("Flood Map")
    canvas.setBackground("blue") #makes window background blue

    canvas.setFill(0, 255, 0)
    for a in range(200, 200) :
        canvas.drawRect(a,a, 100, 100) #attempts to draw land
        w.sleep(1000)    # Time in milliseconds for the window to pause
