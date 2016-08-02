#!/usr/bin/env python

dict = {'ip': '10.10.8.4', 'username': 'ddonaldson', 'password': 'Password123!', 'vendor': 'Aruba', 'model': 'Tester'}
print
print "IP: ", dict['ip']
print "Username: ", dict['username']
print "Password: ", dict['password']
print "Vendor: ", dict['vendor']
print "Model: ", dict['model']
print

### New Password Value ###
dict['password'] = 'Password789!' ##New Password!
print
print "dict['password']: ", dict['password']
print

dict['Secret'] = 'VerySecret'

for key, value in dict.iteritems():
    print key, value

print "Value : %s" % dict.get('device_type', "cisco_ios")

try:
    device_type = dict['device_type']
except KeyError:
    print "Device type not found\n"


