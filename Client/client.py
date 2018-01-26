import socket
import cv2
import os
import numpy

address = ("164.125.35.41",8002)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

capture = cv2.imread("/home/pi/Downloads/0928_3.jpg")

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY), 90]

result, imgencode = cv2.imencode('.jpg', capture, encode_param)
data = numpy.array(imgencode)
stringData = data.tostring()
sock.send(bytes( str(len(stringData)).ljust(16),'utf-8'));
sock.send(bytes( stringData ));

x=sock.recv(1024).decode()
for (i = 1; i <=5; i ++){
    os.system("python led.py")
    }


decimg=cv2.imdecode(data,1)



cv2.imshow('CLIENT', decimg)


sock.close()
cv2.destroyAllWindows()
