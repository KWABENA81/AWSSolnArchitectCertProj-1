import os
import psycopg2

conn = psycopg2.connect(
    host='172.21.0.2',
    database='data_db',
    user='postgres',
    password='password')

#   open cursor for db operations
cur = conn.cursor()

#   execute
cur.execute('DROP TABLE IF EXISTS students;')
cur.execute('CREATE TABLE students ('
            'id serial PRIMARY KEY,'
            'name varchar(100) DEFAULT \'John Doe\' NOT NULL,'
            'city varchar(50)  DEFAULT \'Sunny City\' NOT NULL,'
            'addr varchar(200) DEFAULT \'11 Royal Str\'  NOT NULL,'
            'pin varchar(10)  DEFAULT \'0123\' NOT NULL,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);')

cur.execute('INSERT INTO students (name, city, addr, pin)'
            ' VALUES (\'Anna L\', \'Paris\', \'231 Roma Str\', \'4152\')')

cur.execute('INSERT INTO students (name, city, addr, pin)'
            ' VALUES (\'Cindy L\', \'Frankfurt\', \'231 Roma Str\', \'4152\')')

cur.execute('INSERT INTO students (name, city, addr, pin)'
            ' VALUES (\'Andrew L\', \'Logos\', \'231 Roma Str\', \'4152\')')

conn.commit()

cur.close()
conn.close()
