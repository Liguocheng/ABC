import os

name = '/home/pi/test/test.jpg'
if os.path.exists(name):
    os.remove(name)
