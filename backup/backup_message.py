from twilio.rest import Client 

from twilio.rest import Client

account_sid = 'ACc62f075a13cd277f15cf38859e452faf'
auth_token = 'bb656a225f39a2b049924d3499ef9a0d'
client = Client(account_sid, auth_token)

text_message = "this is your brain speaking"

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=f'{text_message}',
                              to='whatsapp:+447568085248'
                          )

print(message.sid)
