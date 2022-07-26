from twilio.rest import Client

TWILIO_SID = "AC59d26417516ff5e8d77c51b35e391ab2"
TWILIO_AUTH_TOKEN = "522d0d9ed1b0c045cdcc5b11f382037f"
TWILIO_VIRTUAL_NUMBER = "+17314724094"
TWILIO_VERIFIED_NUMBER = "+917902071504"


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
