#!/usr/bin/python3
"""
1-filter_states.py
"""

if __name__ == "__main__":
        import MySQLdb
        from sys import argv

        DataBase = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3])
        cursor = DataBase.cursor()
        cursor.execute("SELECT * FROM states \
        WHERE name LIKE %s ORDER BY id ASC", (argv[4],))
        res = cursor.fetchall()
        for row in res:
                print(row)
                cursor.close()
                DataBase.close()
