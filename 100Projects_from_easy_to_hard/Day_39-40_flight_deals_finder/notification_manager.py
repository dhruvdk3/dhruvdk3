from twilio.rest import Client
twlio_number = "+13137658019"
auth_token = "1b18414b6024ede69ddcfc53b342dc91"
account_sid = "ACc25a1abbacc1396e71f667b020a5ad17"
class NotificationManager:
    def __intit__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twlio_number,
            to="+918788421683",
        )
        # Prints if successfully sent.
        print(message.sid)