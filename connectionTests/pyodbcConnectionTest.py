import pyodbc

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost\SQLEXPRESS;'
    r'DATABASE=model;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
