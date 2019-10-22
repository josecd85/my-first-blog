# myscript.py

from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("DJANGO", "DJANGO", "ENDESA-EVXFBDR2/CFCORCL")

cursor = connection.cursor()
cursor.execute("""
    SELECT first_name, last_name
    FROM employees
    WHERE department_id = :did AND employee_id > :eid""",
    did = 1,
    eid = 0)
for fname, lname in cursor:
    print("Values:", fname, lname)