import os
name = '/home/abc/Graduate/Pic/SerPic.jpg'
if os.path.exists(name):
    os.remove(name)
