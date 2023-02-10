import sqlite3


class TableEmployees(object):
    """Working with employee tabular data"""

    def delete_all(self, conn: sqlite3.connect):
        """Delete all rows from table employees"""
        conn.cursor().execute("""DELETE FROM employees;""")
        conn.commit()

    def insert_one_row(self, conn: sqlite3.connect, row):
        """Insert one row into table employees"""
        ...

    def insert_many_rows(self, conn: sqlite3.connect, rows):
        """Insert many rows into table employees"""
        conn.cursor().executemany("""INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", rows)
        conn.commit()
