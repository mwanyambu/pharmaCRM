import mysql.connector

database = msqyl.connector.connect(
  host="localhost",
  user="root",
  passwd="R00tPassword",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")
