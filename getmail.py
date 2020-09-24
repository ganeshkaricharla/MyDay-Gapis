import Oauth
import os
import pickle
from googleapiclient.discovery import build

def get_servicemail():
    if not os.path.exists('token.pkl'):
        Oauth.get_credentials()
    credentials =pickle.load(open("token.pkl","rb"))
    servicemail = build("gmail","v1" ,credentials=credentials)
    return servicemail


def get_unreadmail(servicemail):
    results = servicemail.users().messages().list(userId='me',labelIds="INBOX", q="is:unread" ).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No New Emails found.')
    else:
        count_unread=len(messages)
        print("You have",count_unread,"New Messages")
        for message in messages:
            msg = servicemail.users().messages().get(userId='me',id=message['id']).execute()
            email_data=msg['payload']['headers']
            for values in email_data:
                typerecv=values['name']
                if typerecv == "From":
                    unreadmsg_sender=values['value']
                    print("You have a message from",unreadmsg_sender)



        


