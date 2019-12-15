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
                charset="utf8",
                db=argv[3])
        cursor = DataBase.cursor()
        cursor.execute("SELECT * FROM states \
        WHERE CONVERT(`name` USING Latin1) \
        COLLATE Latin1_General_CS = '{}';".format(argv[4]))
        states = cur.fetchall()
        for state in states:
                print(state)
