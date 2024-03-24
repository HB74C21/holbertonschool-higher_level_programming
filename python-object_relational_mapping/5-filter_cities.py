#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    user_name = argv[1]
    user_passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user_name, passwd=user_passwd, db=db_name)
    cursor = db.cursor()
    select = "SELECT cities.name from cities INNER JOIN states ON\
        states.id = cities.state_id WHERE states.name = %s\
        ORDER BY cities.id ASC"
    cursor.execute(select, (state_name,))
    cities = cursor.fetchall()
    citiy_list = [citie[0] for citie in cities]
    print(", ".join(citiy_list))
    cursor.close()
    db.close()
