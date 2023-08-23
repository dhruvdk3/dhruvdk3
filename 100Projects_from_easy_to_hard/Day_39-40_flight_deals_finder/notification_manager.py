from twilio.rest import Client
twlio_number = "teilo number"
auth_token = "auth token"
account_sid = "sid"
class NotificationManager:
    def __intit__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twlio_number,
            to="your number",
        )
        # Prints if successfully sent.
        print(message.sid)
