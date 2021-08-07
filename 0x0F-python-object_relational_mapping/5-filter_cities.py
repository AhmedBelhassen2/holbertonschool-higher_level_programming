#!/usr/bin/python3
''' takes in an argument and displays '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query))
    cur.close()
    conn.close()
