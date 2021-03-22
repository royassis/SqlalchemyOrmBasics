from sqlalchemy import create_engine

odbc_connstr = 'mssql+pyodbc://localhost\SQLEXPRESS/testdb?driver=SQL+Server'
engine = create_engine(odbc_connstr, echo=True)

engine.connect()
