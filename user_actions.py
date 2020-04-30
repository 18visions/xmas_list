from users_table import User, userItems
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from config import credential
from datetime import datetime
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
            doesUserExist = session.query(User).filter(User.firstname == firstname).all()
            if not doesUserExist:
                newUser = User(firstname=firstname,
                               lastname=lastname,
                               email=email,
                               phonenumber=phonenumber
                               )
                session.add(newUser)
                session.commit()
                session.close()
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


def create_new_user_item(userId, description, shoppingLink):
    createdate_now = datetime.now()
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            newItem = userItems(userId=userId,
                                description=description,
                                shoppingLink=shoppingLink,
                                dateAdded=createdate_now
                                )
            session.add(newItem)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_new_user_item(1, 'itemstuff', 'www.google.com')
    create_new_user('nick', 'turner', 'test@test.com', '3609493180')
