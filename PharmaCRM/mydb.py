import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="R00tPassword",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")
