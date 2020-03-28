#!/usr/bin/python3
""" script that takes in an argument
    and displays all values in the states
    table of hbtn_0e_0_usa where name
    matches the argument.
"""
import MySQLdb
""" MySQLdb= interface for
    connecting to a MySQL.
"""
import sys
"""sys module provides access to any
    command-line arguments.
"""


if __name__ == "__main__":
    """see if the module has
        been imported or not.
    """
    if len(sys.argv):
        """ date of input """
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        name_of_state = sys.argv[4]
    """ date of input in db """
    db = MySQLdb.connect(host='localhost',
                         user=username, passwd=password, db=database)
    """ var of save date of db.cursor """
    cur = db.cursor()
    """ query for sql in python """
    cur.execute('''SELECT * FROM states
                WHERE name='{}' ORDER BY id ASC'''.format(name_of_state))
    """ recorrer the date of db """
    for row in cur.fetchall():
        print(row)
    """ Close all cursors """
    cur.close()
    """ Close all databases """
    db.close()
