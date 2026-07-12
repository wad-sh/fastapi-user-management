import sqlite3

connect = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER
               )
               """)
connect.commit()
def adduser (name,age) :
    cursor.execute("INSERT INTO users(name,age) VALUES (? , ?)",(name,age))
    connect.commit()
    return cursor.lastrowid

def deleteuser(id) :
    cursor.execute("DELETE FROM users WHERE id = ?",(id,))
    connect.commit()

def updateuser(id,name,age) :
    if name is not None :
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name,id))
        
    if age is not None :
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age,id))
        
    connect.commit()
    

def getallusers () :
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def getuser (id) :
    cursor.execute("SELECT * FROM users WHERE id = ?",(id,))
    return cursor.fetchone()

