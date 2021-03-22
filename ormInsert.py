from sqlalchemy import create_engine
from ormMappers import *
from sqlalchemy.orm import sessionmaker
from faker import Faker
from config import odbc_connstr

faker = Faker()
engine = create_engine(odbc_connstr)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

users = []
for _ in range(5):
    first_name = faker.first_name()
    last_name = faker.last_name()
    full_name = f"{last_name} {first_name}"
    mail1 = faker.email()
    mail2 = faker.email()

    user = User(name=first_name, fullname=full_name, nickname='nickname')
    user.addresses = [Address(email_address=mail1), Address(email_address=mail2)]

    users.append(user)

session.add_all(users)
session.commit()


