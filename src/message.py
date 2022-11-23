from twilio.rest import Client
from revision import Revision
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_AUTH_KEY = os.getenv('TWILIO_AUTH_KEY')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_USER_NUMBER = os.getenv('TWILIO_USER_NUMBER')
TWILIO_SENDER_NUMBER = os.getenv('TWILIO_SENDER_NUMBER')

def message():

    app = Revision()
    revisit = app.get_revisit()
    revision = app.get_revision()
    week = (app.get_week()).upper()
    string = f"Good Morning!\n🗓️week: {week}\n\nRevision: {revision}\nRevisit: {revisit}"

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_KEY)

    message = client.messages.create(
                                  from_=TWILIO_SENDER_NUMBER,
                                  body=string,
                                  to=TWILIO_USER_NUMBER
    )

    del app
