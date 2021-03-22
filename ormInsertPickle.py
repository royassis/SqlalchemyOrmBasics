from sqlalchemy import create_engine
from ormMappers import *
from sqlalchemy.orm import sessionmaker
import pickle

odbc_connstr = 'mssql://localhost\SQLEXPRESS/testdb?driver=SQL+Server'
engine = create_engine(odbc_connstr, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

newmodel = Model(name='newmodel', model='pickledobjectstring')

session.add(newmodel)
session.commit()

model_object = session.query(Model).first()
model = pickle.loads(model_object.model)

print(model)
