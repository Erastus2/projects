import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd= 'korir@21'

)

# prepare cursor object
cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE crmdbs')

print("All done!")