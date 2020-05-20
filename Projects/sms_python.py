from twilio.rest import Client

account = "AC08505b462458dce150355a81bd4f572f"
token = "2cc1b398cc099ef2cf30f9915c408945"
client = Client(account, token)

message = client.messages.create(
                              body='Hi there!',
                              from_='#demo number',
                              to='#any custom number'
                          )
print(message.sid)