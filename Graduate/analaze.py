import os
re_c = os.system('sudo python /home/abc/Graduate/AnaCar/color.py > /home/abc/Graduate/AnaTxt/color.txt')
f_color = open('/home/abc/Graduate/AnaTxt/color.txt')
for line_c in f_color:
    color = line_c.rstrip('\n')
print "ten: " + color
    


re_m = os.system('sudo python /home/abc/Graduate/AnaCar/mark.py > /home/abc/Graduate/AnaTxt/mark.txt')
f_mark = open('/home/abc/Graduate/AnaTxt/mark.txt')
for line_m in f_mark:
    mark = line_m.rstrip('\n')
print "ten:" + mark
    



re_t = os.system('sudo python /home/abc/Graduate/AnaCar/ctype.py > /home/abc/Graduate/AnaTxt/ctype.txt')
f_type = open('/home/abc/Graduate/AnaTxt/ctype.txt')
for line_t in f_type:
    ctype = line_t.rstrip('\n')
print "ten: " + ctype


re_n = os.system('sudo python /home/abc/Graduate/AnaCar/Main.py ')
f = open('/home/abc/Graduate/AnaTxt/getnum.txt','r')
a = f.read()
#for line in a[len(a)::-6]:
a=a[::-1]
a=a[0:4]
a=a[::-1]
print "Opencv: " + a


import time
import datetime
time = "%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

import MySQLdb

db = MySQLdb.connect("localhost","root","123456789","Parking_Management")

cursor = db.cursor()

delete ="""delete from log"""

sql = """INSERT INTO log(get_Time, License_Num, Mark, Color, Car_Type)
         VALUES ( '%s', '%s', '%s','%s', '%s')"""% \
	( time ,a, mark, color, ctype)



cursor.execute(delete)
cursor.execute(sql)
db.commit()
db.rollback()

db.close()


