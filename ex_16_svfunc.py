#!usr/bin/env python

def func_readfile(filename):
    with open(filename) as f:
        return f.read()

def func_findserial(show_ver):
    serial_number = ''
    for line in show_ver.splitlines():
        if 'Processor board ID' in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number

my_file = "show_version.txt"
show_ver = func_readfile(my_file)
serial_number = func_findserial(show_ver)
print "Serial Number is {}\n".format(serial_number)


