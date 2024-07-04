#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
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
    name_search = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password,
        db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` WHERE \
        `name`=%(search)s ORDER BY `id` ASC",
                {'search': name_search})

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
