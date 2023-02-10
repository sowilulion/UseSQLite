import sqlite3


class TableDepartments(object):
    """Working with department tabular data"""

    def delete_all(self, conn: sqlite3.connect):
        """Delete all rows from table departments"""
        conn.cursor().execute("""DELETE FROM departments;""")
        conn.commit()

    def insert_one_row(self, conn: sqlite3.connect, row):
        """Insert one row into table departments"""
        ...

    def insert_many_rows(self, conn: sqlite3.connect, rows):
        """Insert many rows into table departments"""
        conn.cursor().executemany("""INSERT INTO departments VALUES(?, ?, ?);""", rows)
        conn.commit()
