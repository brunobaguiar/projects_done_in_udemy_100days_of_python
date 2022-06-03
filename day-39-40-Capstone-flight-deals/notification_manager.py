from twilio.rest import Client

TWILIO_SID = 'ACa10d9456df04aa1cf8a254dabc06f48d'
TWILIO_AUTH_TOKEN = '3c81b534c1b685b95ae0aac1019f9e08'
TWILIO_VIRTUAL_NUMBER = '+1599999999'
TWILIO_VERIFIED_NUMBER = '+5511999999999'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
