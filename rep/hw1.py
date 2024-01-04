"""port json
c = open(r'C:\Projects\FirstPython\Firsty\venv\Scripts\hw1.txt')
b=open(r'hw1.json','w')
b.write(c.read())"""

import mysql.connector
sql_connection = mysql.connector.connect(user='firstpython3', password='124356qaz', host='db4free.net',
                                             database='firstpython3')
try:
    query_str ='insert into second_table (mon,tue,wed,thu,fri,sat,sun) values (1,2,3,4,5,6,7)'
finally:
    sql_connection.close()