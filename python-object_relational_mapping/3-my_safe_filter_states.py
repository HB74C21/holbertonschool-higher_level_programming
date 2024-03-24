#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one that
is safe from MySQL injections!
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    user_name = argv[1]
    user_passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user_name, passwd=user_passwd, db=db_name)
    cursor = db.cursor()
    select = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(select, (state_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
