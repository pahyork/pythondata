import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()



conn.commit()
conn.close()