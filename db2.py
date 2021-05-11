import sqlite3

conn = sqlite3.connect('emplo.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS Person1""")
cur.execute("""CREATE TABLE Person1
            (name text, age integer, per_id integer)""")

cur.execute("""INSERT INTO Person1 VALUES (?,?,?)""",
                ('pappa', 40, 1001))

cur.execute("""INSERT INTO Person1 VALUES (?,?,?)""",
                ('amma', 23, 1002))

cur.execute("""INSERT INTO Person1 VALUES (?,?,?)""",
                ('anna', 13, 1003))

cur.execute("""INSERT INTO Person1 VALUES (?,?,?)""",
                ('tamma', 8, 1004))

cur.execute("""INSERT INTO Person1 VALUES (?,?,?)""",
                ('tangi', 20, 1005))


conn.commit()
cur = cur.execute("""SELECT * from Person1""")
rows = cur.fetchall()
print('recs:', rows)
conn.close()