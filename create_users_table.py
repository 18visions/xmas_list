from users_table import Base
from sqlalchemy import create_engine
from config import credential
import pyodbc

try:
    engine = create_engine('mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server'
                           .format(credential.dbcreds['username'],
                                   credential.dbcreds['password'],
                                   credential.dbcreds['host'],
                                   credential.dbcreds['port'],
                                   credential.dbcreds['dbname'])
                           )
    Base.metadata.create_all(engine, checkfirst=True)
except Exception as e:
    print(e)
