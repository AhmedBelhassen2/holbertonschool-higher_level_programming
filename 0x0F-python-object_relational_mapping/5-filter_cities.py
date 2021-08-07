#!/usr/bin/python3
''' takes in an argument and displays '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM cities AS c INNER JOIN states AS s ON "
                "c.state_id = s.id WHERE s.name = %s "
                "ORDER BY c.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query))
    cur.close()
    conn.close()
