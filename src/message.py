from twilio.rest import Client
from revision import Revision
import os

def message():

    app = Revision()
    revisit = app.get_revisit()
    revision = app.get_revision()
    week = (app.get_week()).upper()
    string = f"Good Morning!\n🗓️week: {week}\n\nRevision: {revision}\nRevisit: {revisit}"

    sender_number = "(509) 265-6982"
    user_number = "+4407568085248"
    account_sid = os.environ.get('account_sid')
    auth_token = os.environ.get('auth_key') 
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_=sender_number,
                                  body=string,
                                  to=user_number
                              )
    del app
