# Turtle Graphics Documentation

> [!NOTE]
> Over time, this will be my personal Turtle Graphics
> documentation with how to instructions and tips and
> tricks. This is done alongside my programming activities.

## Get Started

```
import turtle
```

## Setup Turtle Graphics Screen

```
screen_x = 512
screen_y = 512
sc = turtle.Screen()
sc.setup(screen_x, screen_y)
```

## Setup Turtle Graphics Window

```
TURTLE_TITLE = "Turtle Graphics Demo"
BACKGROUND_COLOR = "cyan"
turtle.title(TURTLE_TITLE)
turtle.bgcolor(BACKGROUND_COLOR)
```

## Setup a Turtle Screen Object

```
ts = turtle.Turtle()
```

## Add Background to the Window

```
x0, y0 = -int(screen_x/2), -int(screen/2)
x1, y1 = int(screen_x/2), int(screen_y/2)
cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=BG_COLOR, fill=BG_COLOR)
```

## Add Background Correction to the Window

```
pad = 0
x0, y0 = -int(screen_x/2)+pad, -int(screen_y/2)+pad
x1, y1 = int(screen_x/2)-pad, int(screen_y/2)-pad
cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=BG_COLOR, fill=BG_COLOR)
```
