import sqlite3


class Queries(object):
    """Methods with queries"""

    def get_all_companies(self, cur: sqlite3.Cursor):
        """Get all rows from table companies"""
        cur.execute("SELECT id, name, address FROM companies;")
        result = cur.fetchall()
        return result

    def get_all_departments(self, cur: sqlite3.Cursor):
        """Get all rows from table departments"""
        cur.execute("SELECT id, company_id, name FROM departments;")
        result = cur.fetchall()
        return result

    def get_all_employees(self, cur: sqlite3.Cursor):
        """Get all rows from table employees"""
        query = "SELECT id, department_id, name, middle_name, surname, gender, date_start, date_end FROM employees;"
        cur.execute(query)
        result = cur.fetchall()
        return result

    def get_all_departments_with_employees(self, cur: sqlite3.Cursor):
        """Get all departments with employees"""
        cur.execute("""SELECT d.name, COUNT(e.id) as employee_count
               FROM departments d 
                   LEFT JOIN employees e ON e.department_id = d.id
               GROUP BY d.id
               HAVING COUNT(e.id) > 0;""")
        result = cur.fetchall()
        return result
