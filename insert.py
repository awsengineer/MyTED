#!/usr/bin/python34

from htmltag import img, center
import pymysql.cursors
import cgi, cgitb

# Create an instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
fname = form.getvalue('fname')
lname  = form.getvalue('lname')
address  = form.getvalue('address')

db = pymysql.connect(host='RDSEndpoint',
                             user='salehim',
                             password='abcABC123',
                             db='mehdidb',
                             autocommit=True,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
sql='INSERT INTO t1 (fname, lname, address) VALUES ("'+str(fname)+'","'+str(lname)+'","'+str(address)+'")'
cursor.execute(sql)
print ("""
<!DOCTYPE html>
<html>
<body>
<meta HTTP-EQUIV="REFRESH" content="0; url=http:/cgi-bin/ted">
</body>
</html>
""")
