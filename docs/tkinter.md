# Turtle Graphics & Tkinter

## Introductory Words

<p align="justify">Underlying Turtle Graphics 
the module Tkinter further called simply Tkinter 
is used. Things can be achieved via Tkinter that
cannot be achieved via the Turtle Graphics module.
To get control over the Turtle Graphics window one
needs the underlying Tkinter window.</p>

## Get the Turtle Graphics Root Window

<p align="justify">There are two ways to get the
root window. Both are presented subsequently. The
following command returns the Canvas of the invoked
TurtleScreen.</p> 

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
# Get the root window using the Turtle screen.
root = screen._root
```

or in short

```
# Get the root window directly.
root = turtle.getscreen()._root
```

## Show and Hide a Window

<p align="justify">From within Turtle Graphics we are
dealing now with Tkinter. By using the now known root
window we can show and hide the Turtle Graphics window.</p>

```
root.withdraw()
```

<p align="justify">removes the Turtle Graphics
window an</p> 

```
root.deiconify()
```

<p align="justify">restores the window.</p>

<p align="justify">This described behaviour is
not officially documented in the Turtle Graphics
documentations.</p>

## Window Access

<p align="justify">Subsequently I am showing how one 
can access to a Turtle Graphis window and its components.
Figure 1 shows a Turtle Graphics window where I changed
the configuration.</p>

![image](https://github.com/user-attachments/assets/9017e48b-e0aa-41dd-b09f-9659272b0f60)

*Figure 1: Modified Turtle Graphics window*
