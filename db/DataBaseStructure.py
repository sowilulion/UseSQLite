import sqlite3


class DataBaseStructure(object):
    """Data Base Structure"""

    def create_table_companies(self, conn: sqlite3.connect):
        """Create table Companies"""
        conn.cursor().execute("""CREATE TABLE IF NOT EXISTS companies(
                                         id int PRIMARY KEY,
                                         name VARCHAR(100) NOT NULL,
                                         address VARCHAR(100) NOT NULL);""")
        conn.commit()

    def drop_table_companies(self, conn: sqlite3.connect):
        """Drop table Companies"""
        conn.cursor().execute("DROP TABLE companies")
        conn.commit()

    def create_table_departments(self, conn: sqlite3.connect):
        """Create table Companies"""
        conn.cursor().execute("""CREATE TABLE IF NOT EXISTS departments(
                                         id int PRIMARY KEY,
                                         company_id int,
                                         name VARCHAR(100) NOT NULL,
                                         FOREIGN KEY (company_id) REFERENCES companies (id));""")
        conn.commit()

    def drop_table_departments(self, conn: sqlite3.connect):
        """Drop table Companies"""
        conn.cursor().execute("DROP TABLE departments")
        conn.commit()

    def create_table_employees(self, conn: sqlite3.connect):
        """Create table Companies"""
        conn.cursor().execute("""CREATE TABLE IF NOT EXISTS employees(
                                         id int PRIMARY KEY,
                                         department_id int,
                                         name varchar(100) NOT NULL,
                                         middle_name varchar(100) NOT NULL,
                                         surname varchar(100) NOT NULL,
                                         gender char(10) NOT NULL,
                                         date_start date NOT NULL,
                                         date_end date,
                                         FOREIGN KEY (department_id) REFERENCES departments (id));""")
        conn.commit()

    def drop_table_employees(self, conn: sqlite3.connect):
        """Drop table Companies"""
        conn.cursor().execute("DROP TABLE employees")
        conn.commit()
