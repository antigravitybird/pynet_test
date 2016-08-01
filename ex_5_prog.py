#!/usr/bin/env python

### Print File ###
f = open("long_file.md")
for line in f:
    print line.strip ()
f.close ()

### Create New Writable File ###
f = open("new_file.txt", "w")
f.write ("I am a new file\n")
f.close ()

### Append File ###
with open ("new_file.txt", "a") as f:
    f.write ("This is something else in the file\n")
f.close ()
