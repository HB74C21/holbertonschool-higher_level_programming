#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    select = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)
    cursor.execute(select)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
