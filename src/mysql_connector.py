#################################################################################
# Description: This script is used to load the csv data to the mysql database
# Author: Kartikay Singh
# Date: 2024-08-31
#################################################################################
import mysql.connector
from mysql.connector import Error
import sys

database_name = sys.argv[1]
table_name = sys.argv[2]

try:
	# Define connection parameters
	connection = mysql.connector.connect(
		host='localhost',
		user='root',
		# password='root',
		database=database_name
	)

	if connection.is_connected():
		print("Successfully connected to the database")
	print("Database Name: ", database_name)
except Error as e:
	print(f"Error: {e}")

finally:
	if connection.is_connected():
		connection.close()
		print("Connection closed")
  
# interaction with the database

# create a cursor object using the cursor() method
cursor = connection.cursor()

# create a table
cursor.execute(f"CREATE TABLE {table_name} (id INT, name VARCHAR(255), age INT)")

