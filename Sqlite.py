import sqlite3

print("Successfully imported module")

conn = sqlite3.connect("student.db")

print("Database created succesfully!") ; print(type(conn))

cursor = conn.cursor()
print("Cursor created succesfully \n", type(cursor))

