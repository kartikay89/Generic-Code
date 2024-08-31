#################################################################################
# Description: This script is used to load the csv data to the mysql database
# Author: Kartikay Singh
# Date: 2024-08-31
#################################################################################
import mysql.connector
from mysql.connector import Error
import sys

database_name = ""
table_name = ""

try:
	# Define connection parameters
	connection = mysql.connector.connect(
		host='localhost',
		user='root',
		# password='root',
		database='employee_management_system'
	)

	if connection.is_connected():
		print("Successfully connected to the database")

except Error as e:
	print(f"Error: {e}")

finally:
	if connection.is_connected():
		connection.close()
		print("Connection closed")

