import sqlite3
import csv

with sqlite3.connect('./dictionary.db') as conn:
    cursor = conn.cursor()
    
    create_table = '''CREATE TABLE words(
                word TEXT NOT NULL,
                POS TEXT NOT NULL,
                definition TEXT NOT NULL);
                '''
    
    cursor.execute(create_table)
    
    file = open('dictionary.csv')
    contents = csv.reader(file)
    
    insert = "INSERT INTO words (word, POS, definition) VALUES(?,?,?)"
    cursor.executemany(insert, contents)
    
    select_all = "SELECT * FROM words"
    rows = cursor.execute(select_all).fetchall()
    
    conn.commit()
    conn.close()