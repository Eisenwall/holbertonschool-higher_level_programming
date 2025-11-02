#!/usr/bin/python3
"""
Takes a state name as argument and displays all values in the states table
where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from arguments
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

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Use string formatting to create SQL query with user input
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
        state_name
    )
    cursor.execute(query)

    # Fetch all results and print each row
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
