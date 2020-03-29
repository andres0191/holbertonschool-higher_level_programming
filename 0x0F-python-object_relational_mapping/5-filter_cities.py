#!/usr/bin/python3
""" script that takes in the name of a state
    as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
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
    cur.execute('''SELECT name FROM cities WHERE state_id=(SELECT
                    id FROM states WHERE name='{}')'''.format(name_of_state))
    name_city = ""
    for i in cur.fetchall():
        name_city = name_city + i[0] + ", "
    print(name_city[0:-2])
    cur.close()
    db.close()
