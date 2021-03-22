from sqlalchemy import create_engine, LABEL_STYLE_TABLENAME_PLUS_COL
from ormMappers import *
from sqlalchemy.orm import sessionmaker
from faker import Faker
import pandas as pd
from config import odbc_connstr

faker = Faker()
engine = create_engine(odbc_connstr)

Session = sessionmaker(bind=engine)
session = Session()

# Orm query example
for i in session.query(User.name,User.id, Address.id).outerjoin(Address).order_by(User.id.desc()).all():
    print(*i)

# Orm to pandas example
# Set tablename prefix to columns
q = session.query(User, Address).outerjoin(Address).order_by(User.id).set_label_style(LABEL_STYLE_TABLENAME_PLUS_COL)
df = pd.read_sql(q.statement,session.bind)

print(df)