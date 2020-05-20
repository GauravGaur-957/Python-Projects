from twilio.rest import Client

account = "#account"
token = "#token"
client = Client(account, token)

message = client.messages.create(
                              body='Hi there!',
                              from_='#demo number',
                              to='#any custom number'
                          )
print(message.sid)
