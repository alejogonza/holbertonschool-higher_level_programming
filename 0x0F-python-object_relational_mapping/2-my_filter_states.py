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
        cursor.execute("SELECT * FROM states ORDER BY id ASC".format())
        query_rows = cursor.fetchall()
        for row in query_rows:
                if row[1] == argv[4]:
                        print(row)
                        cursor.close()
                        conect.close()
