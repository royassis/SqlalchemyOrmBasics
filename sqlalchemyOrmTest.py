from sqlalchemy import create_engine, text
from ormMappers import *
from sqlalchemy.orm import sessionmaker
from faker import Faker

faker = Faker()
odbc_connstr = 'mssql://localhost\SQLEXPRESS/testdb?driver=SQL+Server'
engine = create_engine(odbc_connstr, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

for _ in range(2):
    first_name = faker.first_name()
    last_name = faker.last_name()
    full_name = f"{last_name} {first_name}"
    mail1 = faker.email()
    mail2 = faker.email()

    user_a = User(name=first_name, fullname=full_name, nickname='nickname')
    user_a.addresses = [Address(email_address=mail1), Address(email_address=mail2)]
    session.add(user_a)

session.commit()

for user, addresses in session.query(User, Address).filter(Address.user_id == None).order_by(User.id).all():
    print(user, addresses)
