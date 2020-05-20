from twilio.rest import Client

account_sid = '#sid'
auth_token = '#auth token'
client = Client('#sid', '#token')

message= client.messages.create(to="#any custom number,
                           from_="#twilio generated number",
                           body="Hello this is Gaurav,I am texting you from my Python Project")

print(message.sid)
