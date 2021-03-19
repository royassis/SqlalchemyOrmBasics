from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Binary
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship("Address", order_by=Address.id, back_populates="user")


class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, Sequence('model_id_seq'), primary_key=True)
    name = Column(String(length=12), nullable=False)
    model = Column(Binary)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.model}')>"


class ModelMetaData(Base):
    __tablename__ = 'modelmetadata'
    id = Column(Integer, primary_key=True)
    extra = Column(String, nullable=False)
    model_id = Column(Integer, ForeignKey('model.id'))

    model = relationship("Model", back_populates="modelmetadata")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.model_id


Model.modelmetadata = relationship("ModelMetaData", order_by=ModelMetaData.id, back_populates="model")
