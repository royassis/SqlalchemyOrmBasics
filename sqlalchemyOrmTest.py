from sqlalchemy import create_engine, text
from ormMappers import *
from sqlalchemy.orm import sessionmaker

odbc_connstr = 'mssql://localhost\SQLEXPRESS/testdb?driver=SQL+Server'
engine = create_engine(odbc_connstr, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

user_a = User(name='Roy', fullname='Assis', nickname='edsnickname')
user_a.addresses = [Address(email_address='jack@google.com'),Address(email_address='jack@google.com')]
user_b = User(name='Moshe', fullname='Assis', nickname='Assis')

session.add(user_a)
session.add(user_b)

# session.query(User).delete()
session.commit()


for user, addresses in session.query(User, Address).filter(User.id==Address.user_id).order_by(User.id).all():
    print(user, addresses)