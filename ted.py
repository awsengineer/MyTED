#!/usr/bin/python34

from htmltag import img, center
from time import gmtime, strftime
import subprocess
import re
import pymysql.cursors

# Connect to the database
db = pymysql.connect(host='RDSEndpoint',
                     user='salehim',
                     password='abcABC123',
                     db='mehdidb',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

print("Content-Type: text/html;charset=utf-8")
print("")

cursor = db.cursor()
cursor.execute("SELECT * from t1")


InstanceID = subprocess.getoutput("curl -s http://169.254.169.254/latest/meta-data/instance-id").replace(" ","")

temp = subprocess.getoutput("curl -s http://169.254.169.254/latest/meta-data/public-ipv4").replace(" ","")
if len(re.findall('404-NotFound',temp)) == 0:
    PublicIP=temp
else:
    PublicIP="N/A"

PrivateIP = subprocess.getoutput("curl -s http://169.254.169.254/latest/meta-data/local-ipv4").replace(" ","")

AZ = subprocess.getoutput("curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone/").replace(" ","")

print ("<br />")

homer=center(img(src="https://raw.githubusercontent.com/awsengineer/CFN/master/Nested/v1.3Show_RDS_data_in_Apache/woohoo.jpg",align="middle",style="width:250;height:200;"))
print (homer)
print ('<html>')
print ('<div align="center"><font size="6">'+"Details of this HTTP Server (behind ELB):"+'</font>')
print ('<head> <style> table, th, td { border: 1px solid brown; } </style> </head>')
print ('<body> <div align="center"> <table bgcolor="#e6ffcc" cellpadding="5" cellspacing="0">')

print ('<tr> <th bgcolor= #ffd1b3><font size="5" color="black">Instance ID</font></th>')
print ('<th bgcolor= #ffd1b3><font size="5" color="black">Public IP</font></th>')
print ('<th bgcolor= #ffd1b3><font size="5" color="black">Private IP</font></th>')
print ('<th bgcolor= #ffd1b3><font size="5" color="black">Availability Zone</font></th>')
print ('<tr color="#804000" align="center">')
print ('<td><font size="5">'+InstanceID+'</font></td>')
print ('<td><font size="5">'+PublicIP+'</font></td>')
print ('<td><font size="5">'+PrivateIP+'</font></td>')
print ('<td> <font size="5">'+AZ+'</font></td>')
print ('</tr>')
print ('</table>')
print ("<br />")
print ("<br />")

print ('<font size="6">'+"The RDS Database Contents:"+'</font>')

print ('<table, th, td { border: 1px solid brown; } </style> </head>')
print ('<body> <div align="center"> <table bgcolor="#e6ffcc" cellpadding="5" cellspacing="0">')
print ('<tr> <th bgcolor= #ffd1b3><font size="5" color="black">First Name</font></th>')
print ('<th bgcolor= #ffd1b3><font size="5" color="black">Last Name</font></th>')
print ('<th bgcolor= #ffd1b3><font size="5" color="black">Address</font></th>')
for row in cursor:
    print ('<tr color="#804000" align="center">')
    print ('<td><font size="5">'+row['fname']+'</font></td>')
    print ('<td><font size="5">'+row['lname']+'</font></td>')
    print ('<td><font size="5">'+row['address']+'</font></td>')


print ('</tr>')
print ('</table>')

print ("<br />")
print ("<br />")
print ('<font size="6">'+"Add a new record:"+'</font>')
print ("<br />")
print ("<br />")

print ('<font size="5" color="black">')
print ('<form action="insert.py"  method="get">')
print ('First name: <input type="text" name="fname" value="">')
print ('Last name:')
print ('<input type="text" name="lname" value="">')
print ('Address:')
print ('<input type="text" name="address" value="">')
print ('<input type="submit" value="Submit">')
print ('</form> ')

print ('</div>')
print ('</body>')
print ('</html>')
db.close()
