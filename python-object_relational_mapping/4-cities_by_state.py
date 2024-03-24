#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    user_name = argv[1]
    user_passwd = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user_name, passwd=user_passwd, db=db_name)
    cursor = db.cursor()
    select = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC"
    cursor.execute(select)
    cities = cursor.fetchall()
    for citie in cities:
        print(citie)
    cursor.close()
    db.close()
