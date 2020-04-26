from users_table import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from os import environ
from config import credential
import pyodbc
import urllib.parse


engine = create_engine('mssql+pyodbc://{}:{}@{}:{}/{}}?driver=SQL+Server'
                       .format(credential.dbcreds['username'],
                               credential.dbcreds['password'],
                               credential.dbcreds['host'],
                               credential.dbcreds['port'],
                               credential.dbcreds['dbname'])
                       )

Base.metadata.create_all(engine, checkfirst=True)
