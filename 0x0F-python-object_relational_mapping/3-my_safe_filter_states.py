#!/usr/bin/python3
"""
This script has similar functionalites
with previous scripts. This time it contains
a set up that make sif free from MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE \
                 BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
