#!/usr/bin/python3
"""
0-select_states.py
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

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        res = cursor.fetchall()
        for row in res:
                print(row)

        cursor.close()
        DataBase.close()
