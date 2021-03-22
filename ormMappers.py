from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, BINARY
from sqlalchemy import ForeignKey, orm
from sqlalchemy.orm import relationship
import pickle

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship("Address",
                             back_populates="user",
                             cascade="all, delete, delete-orphan",
                             passive_deletes=True)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, Sequence('model_id_seq'), primary_key=True)
    name = Column(String(length=12), nullable=False)
    model = Column(BINARY)

    modelmetadata = relationship("ModelMetaData",
                                 back_populates="model",
                                 cascade="all, delete, delete-orphan",
                                 passive_deletes=True)

    def __init__(self, name, model):
        self.name = name
        self.model = self.serialize(model)

    def __repr__(self):
        return f"<Model(name='{self.name}', model='{self.model}')>"

    def serialize(self, obj):
        return pickle.dumps(obj)

    @orm.reconstructor
    def deserialize(self):
        self.model = pickle.loads(self.model)


class ModelMetaData(Base):
    __tablename__ = 'modelmetadata'

    id = Column(Integer, primary_key=True)
    extra = Column(String, nullable=False)
    model_id = Column(Integer, ForeignKey('model.id', ondelete="CASCADE"))

    model = relationship("Model", back_populates="modelmetadata")

    def __repr__(self):
        return f"<ModelMetaData(extra='{self.extra}')>"
