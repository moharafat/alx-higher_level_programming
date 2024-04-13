#!/usr/bin/python3
"""lists all states from database"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("{}".format(sys.argv[0]))
        sys.exit(1)

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()

    query = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()

    
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
