#!/usr/bin/python3
"""
lists all states with a name searched from user input
from the database `hbtn_0e_0_usa`
"""
import MySQLdb
import sys


def main():
    """
    the main function that executes upon request
    :return:
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT c.`name` FROM `states` s LEFT JOIN cities c "
        "ON c.state_id=s.id WHERE s.`name`=%(state_name)s ORDER BY c.`id` ASC",
        {'state_name': state_name})
    query_rows = cur.fetchall()
    print(', '.join([row[0] for row in query_rows]))
    # for row in query_rows:
    #     print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
