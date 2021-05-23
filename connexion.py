import mysql.connector

cnx = mysql.connector.connect(user='', password='',host='127.0.0.1',database='mydb')
cnx.close()