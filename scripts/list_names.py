#!/usr/bin/python

import turtle

names = turtle.__dict__

for c in names:
    if not c.startswith("__") and not c.startswith("_"):
        print(c)
