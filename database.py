import sqlite3

conn = sqlite3.connect(':memory:')

c= conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
              (title TEXT,pages INTEGER)  ''')

# c.execute('INSERT INTO books VALUES("are you my mother?",722)')

books=[
    ('Are you my mother',72),
    ('What the heel is a tuple',92),
    ('Dtabse is exciting',88)
]

c.executemany('INSERT INTO books VALUES (?,?)',books)
conn.commit()        

c.execute('SELECT * FROM books WHERE title="Are you my mother"')
# c.execute('DELETE FROM books WHERE title="Are you my mother"')

c.execute('UPDATE books SET title="New Book" WHERE rowid=2')

dat=c.fetchall()

print(dat)