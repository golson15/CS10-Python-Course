#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:04:32 2019

@author: Grace Olson
"""
#Import the library ezgraphics2 
from ezgraphics2 import GraphicsWindow

#Create a window 
GRAPHICS_WINDOW_HEIGHT = 300
GRAPHICS_WINDOW_WIDTH = 480
win = GraphicsWindow(GRAPHICS_WINDOW_WIDTH, GRAPHICS_WINDOW_HEIGHT)

#Create a white canvas
canvas = win.canvas()
canvas.setColor(255, 0, 255)

#Draw the house
canvas.setOutline("red")
canvas.drawLine(30, 30, 80, 130)
canvas.drawLine(30, 30, 260, 120)
canvas.drawLine(235, 110, 440, 110)
canvas.drawLine(430, 120, 440, 110)
canvas.setOutline("orange")
canvas.drawLine(60, 60, 240, 120)
canvas.drawLine(60, 60, 80, 120)
canvas.drawLine(260, 120, 430, 120)
canvas.setOutline("black")
canvas.setFill("white")
canvas.drawLine(240, 120, 260, 120)
canvas.drawLine(240, 120, 240, 165)
canvas.drawRect(80, 120, 20, 45)
canvas.drawLine(425, 120, 425, 160)
canvas.drawLine(260, 120, 260, 170)
canvas.drawRect(110, 120, 110, 52)
canvas.drawRect(280, 130, 120, 30)
canvas.setOutline("gray")
canvas.setFill("white")
canvas.drawLine(85, 165, 75, 180)
canvas.drawLine(90, 165, 80, 180)
canvas.drawRect(75, 180, 120, 30)
canvas.drawLine(195, 180, 260, 160)
canvas.drawLine(195, 210, 260, 170)
canvas.drawRect(260, 160, 170, 10)

#Add title below it
canvas.drawText(270, 230, "Frank Lloyd Wright House")

#Wait for the user to close the window
win.wait()

