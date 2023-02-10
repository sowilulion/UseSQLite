import sqlite3
from db.DataBaseStructure import DataBaseStructure
from db.dataManipulate.TableCompanies import TableCompanies
from db.dataManipulate.TableEmployees import TableEmployees
from db.dataManipulate.TableDepartments import TableDepartments
from db.Queries import Queries


conn = sqlite3.connect('orders.db')
cur = conn.cursor()

qr = Queries()
tb_comp = TableCompanies()
tb_dep = TableDepartments()
tb_empl = TableEmployees()
dbs = DataBaseStructure()

# dbs.drop_table_companies(conn)
# dbs.drop_table_departments(conn)
# dbs.drop_table_employees(conn)
dbs.create_table_companies(conn)
dbs.create_table_departments(conn)
dbs.create_table_employees(conn)

company_first = (1, "Bread Inc.", "Butter street, container 1")
tb_comp.insert_one_row(conn, company_first)

departments = [(1, 1, "Human Resources"),
               (2, 1, "Sales Department"),
               (3, 1, "Bookkeeping department"),
               (4, 1, "Research & Development")]
tb_dep.insert_many_rows(conn, departments)

employees = [(1, 1, 'Василий', 'Иванович', 'Зайцев', 'Male', '2000-01-01', '2010-01-01'),
             (2, 1, 'Иван', 'Петрович', 'Щебнев', 'Male', '2005-01-01', None),
             (3, 3, 'Елена', 'Владимировна', 'Синицина', 'Female', '2004-01-01', None)]
tb_empl.insert_many_rows(conn, employees)

results = qr.get_all_companies(cur)
print(results)

results = qr.get_all_departments(cur)
print(results)

results = qr.get_all_employees(cur)
print(results)

results = qr.get_all_departments_with_employees(cur)
print(results)

tb_comp.delete_all(conn)
tb_dep.delete_all(conn)
tb_empl.delete_all(conn)

cur.close()
