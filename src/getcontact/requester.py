import json
import time
import requests

from getcontact.cipher import Cipher
from getcontact.config import config


class Requester:
    def __init__(self, config_=None):
        current_config = config_ if config_ else config
        self.cipher = Cipher(current_config)
        self.update_timestamp()
        self.set_dict()

    def set_dict(self):
        self.base_url = "https://pbssrv-centralevents.com"
        self.base_uri_api = f"/{config.API_VERSION}/"
        self.methods = {"number-detail": "details",
                        "search": "search",
                        "verify-code": "",
                        "register": ""}

        self.headers = {"X-App-Version": config.APP_VERSION,
                        "X-Token": config.TOKEN,
                        "X-Os": config.ANDROID_OS,
                        "X-Client-Device-Id": config.DEVICE_ID,
                        "Content-Type": "application/json; charset=utf-8",
                        "Connection": "close",
                        "Accept-Encoding": "gzip, deflate",
                        "X-Req-Timestamp": self.timestamp,
                        "X-Req-Signature": "",
                        "X-Encrypted": "1"}

        self.request_data = {"countryCode": config.COUNTRY,
                             "source": "",
                             "token": config.TOKEN}



    def update_config(self, config):
        self.cipher.update_config(config)
        self.set_dict()

    def update_timestamp(self):
        self.timestamp = str(time.time()).split('.')[0]

    def prepare_payload(self, data):
        return json.dumps(data).replace(" ", "").replace("~", " ")

    def _send_post(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        self.update_timestamp()
        return self._parse_response(response)

    def send_request_encrypted(self, url, data):
        self.headers["X-Encrypted"] = "1"
        return self._send_post(url, json.dumps({"data": self.cipher.encrypt_AES_b64(data)}))

    def send_request_no_encrypted(self, url, data):
        self.headers["X-Encrypted"] = "0"
        return self._send_post(url, data)

    def _parse_response(self, response):
        if response.status_code == 200:
            return True, response.json()["data"]
        if response.status_code == 201:
            return True, response.json()
        else:
            #print(response.text, "error")
            return False, []

    def send_req_to_the_server(self, url, payload, no_encryption=False):
        payload = self.prepare_payload(payload)
        self.headers["X-Req-Signature"] = self.cipher.create_signature(payload, self.timestamp)
        if no_encryption:
            is_ok, response = self.send_request_no_encrypted(url, payload)
        else:
            is_ok, response = self.send_request_encrypted(url, payload)

        if is_ok:
            return json.loads(self.cipher.decrypt_AES_b64(response))
        else:
            return response

    def get_phone_name(self, phoneNumber):
        method = "search"
        self.request_data["source"] = self.methods[method]
        self.request_data["phoneNumber"] = phoneNumber
        return self.send_req_to_the_server(self.base_url + self.base_uri_api + method, self.request_data)

    def get_phone_tags(self, phoneNumber):
        method = "number-detail"
        self.request_data["source"] = self.methods[method]
        self.request_data["phoneNumber"] = phoneNumber
        return self.send_req_to_the_server(self.base_url + self.base_uri_api + method, self.request_data)
