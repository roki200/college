import sqlite3
 
con = sqlite3.connect("test.db")
cursor = con.cursor()
 
cursor.execute("""CREATE TABLE employees
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT, 
                salary REAL)
            """)

staff = [("Вася", 5000), ("Дима", 5000), ("Тима", 5000)]
cursor.executemany("INSERT INTO  employees (name, salary) VALUES (?, ?)", staff)
con.commit()

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())
