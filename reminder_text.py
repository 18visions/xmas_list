import config
from twilio.rest import Client
from user_actions import get_all_user_items, get_user_phone, last_sent_sms
from datetime import datetime, timedelta


def user_reminder(userid):
    useritems = get_all_user_items(userid)
    lastsms = last_sent_sms(userid)
    twentyfourhoursago = datetime.now() - timedelta(hours=24)
    account_sid = config.credential.twiliocreds['acct_sid']
    auth_token = config.credential.twiliocreds['auth_token']
    fromNumber = config.credential.twiliocreds['from_number']
    if useritems:
        pass
    elif not useritems:
        if lastsms < twentyfourhoursago:
            userPhone = get_user_phone(userid)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                to=userPhone,
                from_=fromNumber,
                body="Just a friendly reminder to add items to your Turner family wish list :)")
            print(message.sid)
    elif lastsms < twentyfourhoursago:
        userPhone = get_user_phone(userid)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=userPhone,
            from_=fromNumber,
            body="Just a friendly reminder to add items to your Turner family wish list :)")
        print(message.sid)


if __name__ == '__main__':
    user_reminder(1)  # testing/debugging
