import mysql.connector
# Replace the placeholders with your actual connection details
connection = mysql.connector.connect(
    host='185.30.32.204',
    port=3306,
    database='web46_db16',
    user='web46_16',
    password='1xMJtnzsAEu2QZgN'
)

cursor = connection.cursor()

sql_query = "SHOW TABLES"
cursor.execute(sql_query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()

