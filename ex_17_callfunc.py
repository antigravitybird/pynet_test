#!/usr/bin/env python

def my_func(x, y, z=20):
    return x + y + z

def my_func2(x, y, z=20):
    return x, y, z

print
print "Calling with three positional arguments: "
print "Value: ", my_func(10, 20, 30)
print
print "Calling with two named arguments: "
print "Value: ", my_func(x=10, y=20)
print
print "Calling with one positional argument and two named arguments: "
print "Value: ", my_func(10, y=15, z=55)
print
print "Calling with three strings: "
print "Value: ", my_func(x='happy ', y='little ', z='string')
print
print "Calling with three lists: "
print "Value: ", my_func2(x=['water', 'ice', 'snow'], y=['lava', 'fire', 'steam'], z=['grass', 'soil', 'flora'])
print
print "Making that call more readable: "
ret1, ret2, ret3 = my_func2(x=['water', 'ice', 'snow'], y=['lava', 'fire', 'steam'], z=['grass', 'soil', 'flora'])
print " {}\n {}\n {}".format(ret1, ret2, ret3)
print

