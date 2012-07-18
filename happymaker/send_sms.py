# Download the twilio-python library from http://twilio.com/docs/libraries
# https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest
import twilio

from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account

account = "--"
token = "--"
client = TwilioRestClient(account, token)
 
message = client.sms.messages.create(to="+16198081057", from_="+19177467645",
                                     body="Hello there!")