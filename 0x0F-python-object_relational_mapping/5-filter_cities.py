#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM states " +
                "JOIN cities ON states.id = cities.state_id " +
                "WHERE states.name = %s", (sys.argv[4], ))
    query_rows = cur.fetchall()
    new_list = []
    for row in query_rows:
        new_list.append(row[0])
    print(", ".join(new_list))
    cur.close()
    conn.close()
