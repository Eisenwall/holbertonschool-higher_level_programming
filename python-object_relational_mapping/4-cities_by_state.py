#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa with their state names.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL username, password, and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    # SQL query: join cities and states, order by cities.id
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    # Fetch all results and print each row
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
