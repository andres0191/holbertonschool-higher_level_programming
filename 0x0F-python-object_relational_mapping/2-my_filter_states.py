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
        name_of_state = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute('''SELECT * FROM states
                WHERE name='{}' ORDER BY id ASC'''.format(name_of_state))
    for row in cur.fetchall():
        if row[1] == name_of_state:
            print(row)
    cur.close()
    db.close()
