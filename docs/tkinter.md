hihi# Turtle Graphics & Tkinter

## Introductory Words

<p align="justify">Tkinter is the underlying module behind
Turtle Graphics, from now on simply called Tkinter. Tkinter
can be used to achieve things that are not possible with the
Turtle Graphics module. To gain control over the Turtle
Graphics window, you need the Tkinter window on which this
window is based.</p>

## The Toplevel Window

<p align="justify">Using Tkinter one invokes a top-level window as follows written.</p>

```
root = tk.Tk()
```

<p align="justify">A minimal Python script for creating
two top-level windows looks as follows.</p>

```
#!/usr/bin/python

# Import tkinter as tk.
import tkinter as tk

# Create two top-level windows.
# root = tk.Tk()
win_0 = tk.Tk()
win_1 = tk.Tk()

# Keep the two windows open.
tk.mainloop()
```

<p align="justify">In Tkinter the last command in a script is
 
<pre>tk.mainloop()</pre>

The counterpart of this command in
Turtle Graphics is 

<pre>turtle.mainloop()</pre>
</p>

<p align="justify">What is shown here is not visible done
in the background at Turtle Graphics on start up. For what 
follows one can make use of this behaviour.</p>

## Get the Turtle Graphics Root Window

<p align="justify">There are two ways to get the
Turtle Graphics root window. Both are presented
subsequently. The following command returns the
canvas of the invoked turtle screen.</p> 

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
can get the turtle screen object where the turtle is drawing
on.</p> 

```
# Get the turtle screen.
screen = turtle.getscreen()
```

<p align="justify">Then one can get the root window.</p>

```
# Get the root window using the turtle screen.
root = screen._root
```

<p align="justify">or in short written as</p> 

```
# Get the root window directly.
root = turtle.getscreen()._root
```

## Show and Hide a Root Window

<p align="justify">From within Turtle Graphics we are
dealing now with Tkinter. By using the now known root
window we can show and hide the Turtle Graphics window
like we need this. The command</p>

```
root.withdraw()
```

<p align="justify">removes the Turtle Graphics
window and the command</p> 

```
root.deiconify()
```

<p align="justify">restores the window. Alternatively
one can minimize the window by using the command</p>

```
root.iconify()
```

## Configure the Root Window

root.title("Tkinter & Turtle Graphics Demo")

root.geometry("1366x760+0+0")

root.attributes("-alpha", 0.75)

## Window Access

<p align="justify">Subsequently I am showing how one 
can access a Turtle Graphics window and its components.
Figure 1 shows a Turtle Graphic window where I changed
the configuration.</p>

![image](https://github.com/user-attachments/assets/9017e48b-e0aa-41dd-b09f-9659272b0f60)

*Figure 1: Modified Turtle Graphics window*

First one can idetify the canvas of interest as followed described.

```
for item in root.pack_slaves():
    if isinstance(item, turtle.ScrolledCanvas):
        ScrolledCanvas = item._canvas
```

Then one can configure the canvas.

```
ScrolledCanvas.configure(bg='#00ffff')
ScrolledCanvas.configure(borderwidth=10)
ScrolledCanvas.configure(relief='groove')
ScrolledCanvas.configure(cursor="spider")
```

## Window Data

Screen Data:

- root.winfo_screenwidth()
- root.winfo_screenheight()

Root Position:

- root.winfo_rootx()
- root.winfo_rooty()

Window Data:

- widget.winfo_width()
- widget.winfo_height()

Window Position:

- widget.winfo_x()
- widget.winfo_y()

## Cursors

<p align="justify">The mouse pointer can be changed
by the following command for the root window.</p>

```
root.configure(cursor="mouse")
```
			
| Name                | Name              | Name                |  Name            | Name                 | Name                |    
| :------------------ | :---------------- | :------------------ | :--------------- | :------------------- | :------------------ |
| arrow               | hand1	          | hand2               | mouse            | top_side             | man                 | 
| based_arrow_down    | based_arrow_up    | middlebutton        | umbrella         | top_right_corner     | ul_angle            |
| boat                | pencil            | bogosity            | pirate           | bottom_left_corner   | bottom_right_corner |  
| plus                | question_arrow    | bottom_side         | bottom_tee       | right_ptr            | right_side          | 
| box_spiral          | right_tee         | center_ptr          | rightbutton      | circle               | rtl_logo            | 
| clock               | sailboat          | coffee_mug          | sb_down_arrow    | cross                | cross_reverse       |
| sb_h_double_arrow   | sb_left_arrow     | crosshair           | sb_right_arrow   | diamond_cross        | sb_up_arrow         |
| dot                 | dotbox            | sb_v_double_arrow   | shuttle          | double_arrow         | sizing              | 
| draft_large         | spider            | draft_small         | spraycan         | draped_box	          | star                | 
| exchange            | target            | fleur	        | tcross           | gobbler              | top_left_arrow      |
| gumby	              | top_left_corner   | iron_cross          | heart            | top_tee              | icon                |
| trek                | left_ptr          | X_cursor            | left_side	   | ur_angle             | left_tee	        |
| watch               | leftbutton	  | xterm               | ll_angle	   | lr_angle             |                     |

# References

[1] https://tkdocs.com/shipman/cursors.html
