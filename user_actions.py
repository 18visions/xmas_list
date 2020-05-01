from table_definitions import User, userItems
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
Session = sessionmaker(bind=engine)
session = Session()


def create_new_user(firstname, lastname, email, phonenumber):
    createdate_now = datetime.now()
    try:
        doesUserExist = session.query(User).filter(User.firstname == firstname).all()
        if not doesUserExist:
            newUser = User(firstname=firstname,
                           lastname=lastname,
                           email=email,
                           phonenumber=phonenumber,
                           dateAdded=createdate_now
                            )
            session.add(newUser)
            session.commit()
            session.close()
    except Exception as e:
        print(e)


def create_new_user_item(userId, description, shoppingLink):
    createdate_now = datetime.now()
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


def get_user_item(itemId):
    try:
        getItem = session.query(userItems.itemId).filter(userItems.itemId == itemId).all()
        for x in getItem:
            print(x[0])
            return x[0]
    except Exception as e:
        print(e)


def get_all_user_items(userid):
    try:
        getAll = session.query(userItems).filter(userItems.userId == userid).all()
        for x in getAll:
            print(x)
            return x
    except Exception as e:
        print(e)


def get_user_phone(userid):
    try:
        getPhone = session.query(User.phonenumber).filter(User.userId == userid).all()
        for phone in getPhone:
            return phone[0]
    except Exception as e:
        print(e)


def delete_user_item(uid):
    itemId = uid
    itemToDelete = get_user_item(itemId)
    try:
        getItem = session.query(userItems).filter(userItems.itemId == itemToDelete).delete()
        session.commit()
        session.close()
        print(getItem)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_new_user_item(1, 'itemstuff', 'www.google.com')
    #create_new_user('nick', 'turner', 'test@test.com', '3609493180')
    #get_user_item(8)
    #delete_user_item(5)
    #get_all_user_items(1)
    #get_user_phone(1)
