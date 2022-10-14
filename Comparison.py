# This program is used to compare the  employee information between 180 Engineering and City of Aurora
# 
# 

## SQL Lite Connection ##
import sqlite3

connection = sqlite3.connect("180coa.db")

print(connection.total_changes)

## SQL Table creation ##

cursor = connection.cursor()
cursor.execute("CREATE TABLE contractor (fname TEXT, lname TEXT, title TEXT, hourly FLOAT, benefits TEXT)")
cursor.execute("CREATE TABLE cityemployee (fname TEXT, lname TEXT, title TEXT, hourly FLOAT, benefits TEXT)")

##
