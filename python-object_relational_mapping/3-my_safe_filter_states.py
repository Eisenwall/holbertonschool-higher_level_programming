#!/usr/bin/python3
"""
Safe query: display all values in the states table where name matches
the argument. Protects against MySQL injection by using parameterized
queries (MySQLdb placeholders).
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Command-line arguments: username, password, database, state name
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

    # Parameterized query prevents SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
