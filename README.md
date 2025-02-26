# Inofficial Turtle Graphics Documentation

> [!NOTE]
> 🚧 Over time, this will be my personal Turtle Graphics
> documentation with how to instructions and tips and
> tricks. This is done alongside my programming activities.

## 🐢 Turtle Graphics

This documentation is related to the Python standard turtle library [1].

## 🚀 Getting Started

Import the standard Python module turtle to get started.

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

After initialising the screen we will need the screen object sc 
no longer. The screen setup is done at this point.

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

For adding a background to the window one is using a canvas from 
tkinter. The rectangle canvas is what one needs for this goal.

```
bg_color
x0, y0 = -int(screen_x/2), -int(screen_y/2)
x1, y1 = int(screen_x/2), int(screen_y/2)
cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=bg_color, fill=bg_color)
```

By adding a rectangle one can change the background. The reason is explained later.

## Putting the Things Together

![image](https://github.com/user-attachments/assets/e2c6b664-2a42-40cd-bd7e-c98d6a0bbbbc)

In this window we see something that we should not see. 
The background is not completely blue as it should be We
see something like a border in red which is 1 point thick.
This thin border in particular causes difficulties later on.

## Add a Background Correction to the Window

```
pad = 6
x0, y0 = -int(screen_x/2)+pad, -int(screen_y/2)+pad
x1, y1 = int(screen_x/2)-pad, int(screen_y/2)-pad
cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=BG_COLOR, fill=BG_COLOR)
```
This modifies the rectangle in a way, that one has a one pixel border around the 
drawing area. The reason is explained later.

## Putting the Things Together

![image](https://github.com/user-attachments/assets/fbf745ff-9471-43b5-ba61-574e8eb805f5)

If one inspects the behaviour of the frame one sees that 
two sides show 2 pixel width and the other two sides 6 pixel
width which should normally not happened. 


## Interactive Turtle Graphics

Open a Python console and you can try out command in this console while a Turtle Graphics 
window is open.

## Some Commands

| METHOD       | PARAMETER  | DESCRIPTION |
| :----------: | :--------: | :---------: |
| Turtle()	    | None	      | Creates and returns a new turtle object                        |
| home()       | None       | Move turtle to the origin (0,0)                                |
| forward()	   | amount     |	Moves the turtle forward by the specified amount               |
| fd()	        | amount     |	Moves the turtle forward by the specified amount               |
| backward()	  | amount	    | Moves the turtle backward by the specified amount              |
| back()	      | amount	    | Moves the turtle backward by the specified amount              |
| bk()	        | amount	    | Moves the turtle backward by the specified amount              |
| right()	     | angle  	   | Turns the turtle clockwise                                     |
| left()	      | angle	     | Turns the turtle counter clockwise                             |
| penup()	     | None	      | Picks up the turtle’s Pen                                      |
| up()	        | None	      | Picks up the turtle’s Pen                                      |
| pendown()	   | None	      | Puts down the turtle’s Pen                                     |
| down()	      | None	      | Puts down the turtle’s Pen                                     |
| color()	     | color name | Changes the color of the turtle’s pen                          |
| fillcolor()  |	color name |	Changes the color of the turtle will use to fill a polygon     |
| heading()	   | None	      | Sets and returns the current heading                           |
| seth()	      | None	      | Sets and returns the current heading                           |
| position()	  | None	      | Returns the current position                                   |
| goto()	      | x, y	      | Moves the turtle to position x,y                               |
| begin_fill() | None 	     | Remember the starting point for a filled polygon               |
| end_fill()	  | None	      | Closes the polygon and fills with the current fillcolor        |
| dot()	       | None	      | Prints a dot at the current position                           |
| stamp()	     | None	      | Prints an impression of a turtle shape at the current location |
| shape()      | shapename	 | Should be 'turtle', 'arrow', 'classic' or 'circle'             |


Not working commands from the documentation:

| METHOD       | PARAMETER  | DESCRIPTION |
| :----------: | :--------: | :---------: |
| teleport()   | x,y	 | Moves the turtle to position x,y without printing |

## Turtle Version

One gets the turtle version by the command: 

<pre>print(turtle._ver)</pre>

In my case the result looks like:

<pre>turtle 1.1b- - for Python 3.1   -  4. 5. 2009</pre>

## Radians Versus Degrees

Turn turtle right or turn turtle left can be done by angle units.
Angle units by default are in degrees, but can be set via the 
degrees() or radians() functions to each other.

# References

[1] https://docs.python.org/3/library/turtle.html

[2] https://compform.net/turtles/

[3] https://el.media.mit.edu/logo-foundation/what_is_logo/index.html

 
