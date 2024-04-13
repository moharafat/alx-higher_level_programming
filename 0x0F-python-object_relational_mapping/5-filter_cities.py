#!/usr/bin/python3
"""lists all states from database"""
import MySQLdb
import sys
if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")

    cur = conn.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""",(sys.argv[4],))
    query_rows = cur.fetchall()
    The_Cities = []
    for row in query_rows:
        The_Cities.append(row[0])
    print(*The_Cities, sep=", ")
    cur.close()
    conn.close()
