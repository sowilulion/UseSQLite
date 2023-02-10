import sqlite3


class TableCompanies(object):
    """Working with company tabular data"""

    def delete_all(self, conn: sqlite3.connect):
        """Delete all rows from table companies"""
        conn.cursor().execute("""DELETE FROM companies;""")
        conn.commit()

    def insert_one_row(self, conn: sqlite3.connect, row):
        """Insert one row into table companies"""
        conn.cursor().execute("""INSERT INTO companies VALUES(?, ?, ?);""", row)
        conn.commit()

    def insert_many_rows(self, conn: sqlite3.connect, rows):
        """Insert many rows into table companies"""
        ...
