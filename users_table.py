from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer,
                primary_key=True,
                nullable=False)
    firstname = Column(String(100),
                  nullable=False)
    lastname = Column(String(100),
                      nullable=False)
    email = Column(String,
                 nullable=False)
    phonenumber = Column(String,
                    nullable=False)

    def __repr__(self):
        return '<Example model {}>'.format(self.id)
