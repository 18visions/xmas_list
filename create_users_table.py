from users_table import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from os import environ
from config import credential
import pyodbc
import urllib.parse


engine = create_engine('mssql+pyodbc://{}:{}@{}:{}/xmas_list?driver=SQL+Server'
                       .format(credential.dbcreds['username'],
                               credential.dbcreds['password'],
                               credential.dbcreds['host'],
                               credential.dbcreds['port'])
                       )

Base.metadata.create_all(engine, checkfirst=True)
