#!/usr/bin/python3
""" script that takes in an argument
    and displays all values in the states
    table of hbtn_0e_0_usa where name
    matches the argument.
"""


import MySQLdb
import sys


if __name__ == "__main__":

    if len(sys.argv):
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute('''SELECT * FROM states
                WHERE name LIKE 'N%' ORDER BY id ASC''')
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
