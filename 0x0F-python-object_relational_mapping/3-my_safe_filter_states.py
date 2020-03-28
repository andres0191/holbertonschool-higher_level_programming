#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv):
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        name_of_state = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states
                WHERE name='{}' ORDER BY states.id ASC".format(name_of_state,))
    for row in cur.fetchall():
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()