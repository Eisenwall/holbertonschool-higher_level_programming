#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves all states
from the hbtn_0e_0_usa database, ordered by the state id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_pass, db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get all states sorted by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
