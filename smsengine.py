from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection

class SmsEngine():
    def __init__(self, logger):
        self.logger = logger

    def send_message(self):
        with Connection('http://admin:MY_SUPER_TRUPER_PASSWORD@192.168.8.1/') as connection:
            client = Client(connection)
            response = client.sms.send_sms("phone_numbers", "message")
            print(client.device.signal())  # Can be accessed without authorization
            # Needs valid authorization, will throw exception if invalid credentials are passed in URL
            print(client.device.information())

        
