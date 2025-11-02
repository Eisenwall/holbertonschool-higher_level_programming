#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection using parameterized queries.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name
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

    # Parameterized query: join cities and states, filter by state name
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    # Fetch results and print city names separated by commas
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()
