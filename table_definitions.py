from sqlalchemy import Column, Integer, String, DateTime, func, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema": "dbo"}

    userId = Column(Integer,
                    primary_key=True,
                    nullable=False)
    firstname = Column(String(100),
                       nullable=False)
    lastname = Column(String(100),
                      nullable=False)
    email = Column(String(100),
                   nullable=True)
    phonenumber = Column(String(100),
                         nullable=False)
    dateAdded = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    #def __repr__(self):
    #    return '<User {}>'.format(self.id)


class userItems(Base):
    __tablename__ = "userItems"
    __table_args__ = {"schema": "dbo"}
    itemId = Column(Integer,
                    primary_key=True,
                    nullable=False)
    userId = Column(Integer,
                    nullable=False)
    description = Column(String(1000),
                         nullable=True)
    shoppingLink = Column(String(1000),
                          nullable=True)
    dateAdded = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    def __repr__(self):
        return '<User Items: itemId: {}, description: {}>'.format(self.itemId, self.description)


class smsmessages(Base):
    __tablename__ = 'smsMessages'
    __table_args__ = {"schema": "dbo"}
    userId = Column(Integer,
                    primary_key=False,
                    nullable=False)
    toNumber = Column(String(100),
                      nullable=False)
    twilioSid = Column(String(100),
                       primary_key=True)
    dateSent = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())
