# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACf61c0c0deb91e3cfc8d182511490864b", "dae0155580e256cba9b60672db8281c7")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+12697795759", 
                       from_="+12542551518", 
                       body="Hello from Python!")