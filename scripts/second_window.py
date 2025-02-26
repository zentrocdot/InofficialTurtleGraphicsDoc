#!/usr/bin/python

import turtle

screen_x = 512
screen_y = 512

sc = turtle.Screen()
sc.setup(screen_x, screen_y)

window_title = "Second Turtle Graphics Demo"
background_color = "red"

turtle.title(window_title)
turtle.bgcolor(background_color)

ts = turtle.Turtle()

x0, y0 = -int(screen_x/2), -int(screen_x/2)
x1, y1 = int(screen_x/2), int(screen_y/2)
bg_color = "blue"

cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=bg_color, fill=bg_color)

turtle.done()
