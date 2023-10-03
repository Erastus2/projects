import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd= 'korir@21'

)

# prepare cursor object
cursorObject = dataBase.cursor()
# create a database
cursorObject.execute('CREATE DATABASE crm')

print("All done!")