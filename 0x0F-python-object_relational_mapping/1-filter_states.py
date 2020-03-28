#!/usr/bin/python3
""" script that lists all states with
    a name starting with N (upper N) from
    the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    """ see if the module has been imported or not. """
    if len(sys.argv):
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         user=username, passwd=passwd, db=database)
    cur = db.cursor()
    cur.execute('''SELECT * FROM states
                WHERE name LIKE 'N%' ORDER BY id ASC''')
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)
