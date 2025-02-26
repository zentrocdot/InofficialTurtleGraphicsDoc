# Turtle Graphics Documentation

> [!NOTE]
> Over time, this will be my personal Turtle Graphics
> documentation with how to instructions and tips and
> tricks. This is done alongside my programming activities.

## Get Started

```
import turtle
```

After importing the standard Python module turtle
one is ready to use Turtle graphics.

## Setup Turtle Graphics Screen

```
screen_x = 512
screen_y = 512
sc = turtle.Screen()
sc.setup(screen_x, screen_y)
```

Based on my monitor which has a resolution of 1366 x 768 pixel
I have chosen a square Turtle Graphics screen with a resolution
of 512 x 512 pixel.

## Setup Turtle Graphics Window

```
window_title = "Turtle Graphics Demo"
background_color = "red"
turtle.title(window_title)
turtle.bgcolor(background_color)
```

This is changing the title of the Turtle Graphics window.
The background color is also changed from white to red.

## Putting the Things Together

![image](https://github.com/user-attachments/assets/04e7ac38-9bd0-4693-8eb6-115bf8442e7c)

The frame type for the drawing area we can see is so-called sunken. 
At the top and at the left there is a dark shadow. At the bottom and
at the right there is a light shadow. 

## Setup a Turtle Screen Object

```
ts = turtle.Turtle()
```

To use Turtle Graphics one need a turtle (screen) object.

## Add Background to the Window

```
bg_color
x0, y0 = -int(screen_x/2), -int(screen_y/2)
x1, y1 = int(screen_x/2), int(screen_y/2)
cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=bg_color, fill=bg_color)
```

By adding a rectangle one can change the background. The reason is explained later.

## Add Background Correction to the Window

```
pad = 0
x0, y0 = -int(screen_x/2)+pad, -int(screen_y/2)+pad
x1, y1 = int(screen_x/2)-pad, int(screen_y/2)-pad
cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=BG_COLOR, fill=BG_COLOR)
```
This modifies the rectangle in a way, that one has a one pixel border around the 
drawing area. The reason is explained later.

## Putting the Things Together

![image](https://github.com/user-attachments/assets/e2c6b664-2a42-40cd-bd7e-c98d6a0bbbbc)

