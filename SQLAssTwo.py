import sqlite3

print("Successfully imported module")

conn = sqlite3.connect("SGA_1_3_.db")

print("Database created succesfully!") ; print(type(conn))

cursor = conn.cursor()
print("Cursor created succesfully \n", type(cursor))

cursor.execute("""
                 CREATE TABLE GroupLessonTwo (
                         first_name text,
                         last_name text,
                         email text,
                         course ext,
                         phone_number integer
                  ) 
""")

cursor.execute("""
                INSERT INTO GroupLessonTwo VALUES ('Awoniran','Omowunmi','awoniranwunmi@gmail.com', 'Data Science', '08132958070')  
""")
cursor.execute("""
                INSERT INTO GroupLessonTwo VALUES ('Binta','Umar','umar@gmail.com', 'Data Science', '08027284588')  
""")
cursor.execute("""
                INSERT INTO GroupLessonTwo VALUES ('Esther','Akpanowo','estherakpan@gmail.com', 'Data Science', '09077546691')  
""")

cursor.execute("SELECT * from GroupLessonTwo")

print("Succesful")

conn.commit()



