from twilio.rest import Client
from revision import Revision

def message():

    app = Revision()
    revisit = app.get_revisit()
    revision = app.get_revision()
    week = app.get_week()

    string = f"Good Morning!\n\nWeek: {week.upper()}\n\nRevision: {revision}\nRevisit: {revisit}\n\nSend 'done' when task completed✅\n\n"


    account_sid = 'ACc62f075a13cd277f15cf38859e452faf'
    auth_token = 'bb656a225f39a2b049924d3499ef9a0d'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  messaging_service_sid='MG6d28a5c3409174ae1e82202252e37c00',
                                  body=f'{string}',
                                  to='+4407568085248'
                              )
message()
