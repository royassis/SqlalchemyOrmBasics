from sqlalchemy import create_engine, text
from ormMappers import *
from sqlalchemy.orm import sessionmaker

odbc_connstr = 'mssql://localhost\SQLEXPRESS/testdb?driver=SQL+Server'
engine = create_engine(odbc_connstr, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

ed_user = User(name='aa', fullname='Ed Jones', nickname='edsnickname')
ed_user.addresses = [Address(email_address='jack@google.com'),Address(email_address='jack@google.com')]

session.add(ed_user)
session.commit()

for user, addresses in session.query(User, Address).filter(User.id==Address.user_id).order_by(User.id).all():
    print(user, addresses)