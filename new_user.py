from users_table import User
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from config import credential
import pyodbc


engine = create_engine('mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server'
                       .format(credential.dbcreds['username'],
                               credential.dbcreds['password'],
                               credential.dbcreds['host'],
                               credential.dbcreds['port'],
                               credential.dbcreds['dbname']))


def create_new_user(firstname, lastname, email, phonenumber):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            doesUserExist = session.query(exists().where(User.firstname == firstname))
            if not doesUserExist:
                newUser = User(firstname=firstname,
                               lastname=lastname,
                               email=email,
                               phonenumber=phonenumber
                               )
                session.add(newUser)
                session.commit()
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_new_user('aaa', 'aaa', 'abc', 'xyz')
