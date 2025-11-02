#!/usr/bin/python3
"""
Takes a state name as argument and displays all values in the states table
where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    # SQL query using format to include user input
    query = ("SELECT * FROM states WHERE name='{}' "
             "ORDER BY id ASC").format(state_name)
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
