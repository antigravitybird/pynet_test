#!/usr/bin/env python

def new_func(x, y, z=20):
    return x + y + z

new_list = (3, 7, 21)
new_dict = {
    'x' : 5,
    'y' : 29,
    'z' : 1,
}

print
print "Calling with *args"
print "Value: ", new_func(*new_list)
print
print "Calling with **kwargs"
print "Value: ", new_func(**new_dict)
print
