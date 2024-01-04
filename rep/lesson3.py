import mysql.connector

try:
    sql_connection = mysql.connector.connect(user='firstpython3', password='124356qaz', host='db4free.net',
                                             database='firstpython3')
except Exception as err:
    print(err)
try:
    query_str = 'SELECT name1, number2 FROM first_table'
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute(query_str)
    for (name1, number2) in sql_cursor:
        print(f'name: {name1}, number: {number2}')
except Exception as err:
    print(err)
finally:
    sql_connection.close()

