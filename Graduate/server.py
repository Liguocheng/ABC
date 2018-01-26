import socket
import cv2
import numpy
import os


address = ('164.125.35.41', 8002)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(True)

def revcall(sock, count):
    buf = b''
    while count:        
        newbuf=sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

#conn, addr = s.accept()


while True:
	print "Waiting for img"	
	conn, addr = s.accept()
	length = revcall(conn,16)
	stringData = revcall(conn, int(length))
	data = numpy.fromstring(stringData, dtype='uint8')




	decimg = cv2.imdecode(data,1)
	cv2.imwrite("/home/abc/Graduate/Pic/SerPic.jpg" , decimg ,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
	print"Save Result to database"
	os.system('sudo python /home/abc/Graduate/analaze.py')

	print"Delete img"
	os.system('sudo python /home/abc/Graduate/checks.py')
	
	x = '1'
	conn.send(x.encode())
	
s.close()
cv2.destroyAllWindows()

