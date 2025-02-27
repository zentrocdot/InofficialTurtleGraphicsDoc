# Unofficial Turtle Graphics Docs
> [!NOTE]
> <p align="justify">🚧 Over time, this will be my personal
> Turtle Graphics documentation with how to instructions
> and tips and tricks. This is done alongside my programming
> activities.</p>

![ComfyUI_00953_](https://github.com/user-attachments/assets/5d5212ed-1311-46b1-8441-489c0a87b425)

## 🐢 Turtle Graphics

<p align="justify">This documentation is related to the Python 
standard turtle library [1].</p>

## 🚀 Getting Started

<p align="justify">Import the standard Python module turtle 
to get started.</p>

```
import turtle
```

<p align="justify">After importing the standard Python 
module turtle one is ready to use Turtle Graphics for
creating images.</p>

## Setup Turtle Graphics Screen

```
screen_x = 512
screen_y = 512

sc = turtle.Screen()
sc.setup(screen_x, screen_y)
```

<p align="justify">Based on my monitor which has a resolution
of 1366 x 768 pixel I have chosen a square Turtle Graphics
screen with a resolution of 512 x 512 pixel. After initialising
the screen we will need the screen object sc no longer. The 
screen setup is done at this point.</p>

## Setup Turtle Graphics Window

```
window_title = "Turtle Graphics Demo"
background_color = "red"

turtle.title(window_title)
turtle.bgcolor(background_color)
```

<p align="justify">This is changing the title of the Turtle
Graphics window. The background color is also changed from
white to red.</p>

## Putting the Things Together

![image](https://github.com/user-attachments/assets/04e7ac38-9bd0-4693-8eb6-115bf8442e7c)

<p align="justify">The frame type for the drawing area we 
can see is so-called sunken. At the top and at the left
there is a dark shadow. At the bottom and at the right
there is a light shadow.</p> 

## Setup a Turtle Screen Object

```
ts = turtle.Turtle()
```

<p align="justify">To use Turtle Graphics one need a turtle
(screen) object.</p> 

## Add Background to the Window

<p align="justify">For adding a background to the window
one is using a canvas from tkinter. The rectangle canvas
is what one needs for this goal.</p> 

```
bg_color
x0, y0 = -int(screen_x/2), -int(screen_y/2)
x1, y1 = int(screen_x/2), int(screen_y/2)

cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=bg_color, fill=bg_color)
```

<p align="justify">By adding a rectangle one can change
the background. The reason is explained later.</p> 

## Putting the Things Together

![image](https://github.com/user-attachments/assets/e2c6b664-2a42-40cd-bd7e-c98d6a0bbbbc)

<p align="justify">In this window we see something that
we should not see. The background is not completely blue
as it should be We see something like a border in red
which is 2 point thick. This thin border in particular
causes difficulties later on.</p> 

## Add a Background Correction to the Window

```
pad = 6
x0, y0 = -int(screen_x/2)+pad, -int(screen_y/2)+pad
x1, y1 = int(screen_x/2)-pad, int(screen_y/2)-pad

cs = ts.getscreen()
tkwin = cs.getcanvas()
tkwin.create_rectangle(x0, y0, x1, y1, width=0, outline=BG_COLOR, fill=BG_COLOR)
```

<p align="justify">This modifies the rectangle in a way,
that one has a two pixel border (plus 4 pixel)
around the drawing area. The reason is explained later.</p> 

## Putting the Things Together

![image](https://github.com/user-attachments/assets/fbf745ff-9471-43b5-ba61-574e8eb805f5)

<p align="justify">If one inspects the behaviour of the frame
one sees that two sides show 2 pixel width and the other two
sides 6 pixel width which should normally not happened. 2 sides
show a discrepancy of 4 pixels. Whether this is a Turtle Graphics
error or a Tkinter error is not yet clear.</p> 

<p align="justify">One result next to the later discussed problem is,
that an object is never centered in the screen.</p> 

## Interactive Turtle Graphics

<p align="justify">Open a Python console and you can try out command in this console while a Turtle Graphics 
window is open.</p> 

## Some Commands

| METHOD              | PARAMETER   | DESCRIPTION |
| :-----------------: | :---------: | :---------: |
| Turtle()	          | None	      | Creates and returns a new turtle object                                        |
| home()              | None        | Move turtle to the origin (0,0)                                                |
| forward(distance)   | amount      |	Moves the turtle forward by the specified amount                               |
| fd(distance)	      | amount      |	Moves the turtle forward by the specified amount                               |
| backward(distance)  | amount	    | Moves the turtle backward by the specified amount                              |
| back(distance)	    | amount	    | Moves the turtle backward by the specified amount                              |
| bk(distance)	      | amount	    | Moves the turtle backward by the specified amount                              |
| right(angle)	      | angle  	    | Turns the turtle clockwise                                                     |
| rt(angle)	          | angle  	    | Turns the turtle clockwise                                                     |
| left(angle)         | angle	      | Turns the turtle counter clockwise                                             |
| lt(angle)           | angle	      | Turns the turtle counter clockwise                                             |
| penup()	            | None	      | Picks up the turtle’s Pen                                                      |
| up()	              | None	      | Picks up the turtle’s Pen                                                      |
| pendown()	          | None	      | Puts down the turtle’s Pen                                                     |
| down()	            | None	      | Puts down the turtle’s Pen                                                     |
| color(*args)	      | color name  | Returns or sets pen color and fill color                                       |
| pencolor(*args)	    | color name  | Returns or sets pen color                                                      |
| fillcolor(*args)    |	color name  |	Returns or sets the fill color                                                 |
| heading()	          | None	      | Sets and returns the current heading                                           |
| seth()	            | None	      | Sets and returns the current heading                                           |
| position()	        | None	      | Returns the current position                                                   |
| goto()	            | x, y	      | Moves the turtle to position x,y                                               |
| begin_fill()        | None 	      | Remember the starting point for a filled polygon                               |
| end_fill()	        | None	      | Closes the polygon and fills with the current fillcolor                        |
| dot()	              | None	      | Prints a dot at the current position                                           |
| stamp()	            | None	      | Prints an impression of a turtle shape at the current location                 |
| shape()             | shapename	  | Can be 'turtle', 'arrow', 'classic', 'circle', 'square', 'triangle' or 'blank' |
| xcor()              | None        | Get the x-coordinate of the turtle                                             |
| ycor()              | None        | Get the y-coordinate of the turtle                                             |

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

<p align="justify">Turn turtle right or turn turtle left can 
be done by angle units. Angle units by default are in degrees,
but can be set via the degrees() or radians() functions to each
other.</p> 

## Pictures

<p align="justify">One can add pictures to the window. This is 
done by the following command.</p> 

<pre>sc.bgpic("test.gif")</pre>

![image](https://github.com/user-attachments/assets/1f6763fb-1079-4ef4-97a4-d1ae8d42eb39)

## Colors

<p align="justify">Colors can be set using RGB color tuples
like (255, 0, 0) which is red. Names can be used like 'blue' 
or one can use a HEX representation like '#00FF00' which is
lime.</p> 

## Get the Turtle Graphics Root Window

<p align="justify">To get control over the Turtle Graphics
window one needs the underlying Tkinter window. There are 
two ways to get the root window. Both are presented 
subsequently. The following command returns the Canvas of
the invoked TurtleScreen.</p> 

```
# Get screen canvas.
canvas = turtle.getcanvas()
```

<p align="justify">Then one can get the root window directly.
This way is the way one should use to get the root window.</p> 

```
# Get the root window.
root = canvas.winfo_toplevel()
```

<p align="justify">The other way is not the proposed way, it 
makes use of a protected member of a client class. First one
can get the Turtle screen object where the turtle is drawing
on.</p> 

```
# Get the Turtle screen.
screen = turtle.getscreen()
```

<p align="justify">Then one can get the root window.</p>

```
# Get the root window.
root = screen._root

or in short

# Get the root window.
root = turtle.getscreen()._root
```

## Helper Functions

### Color To RGB Function

This function needs the Python package webcolors. The goal
is to return a color tuple from an arbitrary color input.

```
def color_to_rgb(color):
    # Try to get the RGB color.
    try:
        # Check the type of the color.
        if color is not None:
            if color.startswith('#'):
                rgb = webcolors.hex_to_rgb(color)
            elif color is None or isinstance(color, (list, tuple)):
                rgb = color
            elif isinstance(color, str):
                rgb = webcolors.name_to_rgb(color)
            # Get the RGB components.
            r,g,b = rgb[0], rgb[1], rgb[2]
        else:
            r,g,b = 0,0,0
    except:
        r,g,b = 0,0,0
    # Return the RGB color tuple.
    return r,g,b
```

# References

[1] https://docs.python.org/3/library/turtle.html

[2] https://compform.net/turtles/

[3] https://el.media.mit.edu/logo-foundation/what_is_logo/index.html
