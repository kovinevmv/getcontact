import json
import time

import requests
from getcontact.cipher import Cipher
from getcontact.config import config
from getcontact.config_updater import UpdateConfig
from getcontact.logger import Log


class Requester:
    def __init__(self, config_=None):
        current_config = config_ if config_ else config
        self.cipher = Cipher(current_config)
        self.updater = UpdateConfig()
        self.update_timestamp()
        self.set_dict()

    def set_dict(self):
        self.base_url = "https://pbssrv-centralevents.com"
        self.base_uri_api = f"/{config.API_VERSION}/"
        self.methods = {
            "number-detail": "details",
            "search": "search",
            "verify-code": "",
            "register": "",
        }

        self.headers = {
            "X-App-Version": config.APP_VERSION,
            "X-Token": config.TOKEN,
            "X-Os": config.ANDROID_OS,
            "X-Client-Device-Id": config.DEVICE_ID,
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate",
            "X-Req-Timestamp": self.timestamp,
            "X-Req-Signature": "",
            "X-Encrypted": "1",
        }

        self.request_data = {
            "countryCode": config.COUNTRY,
            "source": "",
            "token": config.TOKEN,
        }

    def update_config(self, config_):
        self.cipher.update_config(config_)
        self.set_dict()

    def update_timestamp(self):
        self.timestamp = str(time.time()).split(".")[0]

    def prepare_payload(self, data):
        return json.dumps(data).replace(" ", "").replace("~", " ")

    def _send_post(self, url, data):
        Log.d("Call _send_post with url:", url, "data:", data)
        response = requests.post(url, data=data, headers=self.headers)
        self.update_timestamp()
        return self._parse_response(response)

    def send_request_encrypted(self, url, data):
        self.headers["X-Encrypted"] = "1"
        return self._send_post(
            url, json.dumps({"data": self.cipher.encrypt_AES_b64(data)})
        )

    def send_request_no_encrypted(self, url, data):
        self.headers["X-Encrypted"] = "0"
        return self._send_post(url, data)

    def _parse_response(self, response):
        Log.d("Call _parse_response with response:", response.text)

        if response.status_code == 200:
            return True, response.json()["data"]
        if response.status_code == 201:
            return True, response.json()

        Log.d("Not correct answer from server.")
        response = response.json()
        if "data" in response.keys():
            response = response["data"]
            Log.d("Response: ", response)

            response = json.loads(self.cipher.decrypt_AES_b64(response))
            Log.d("Response decrypted: ", response)

            errorCode = response["meta"]["errorCode"]

            if errorCode == "403004":
                print("Captcha is detected. ")
                from getcontact.decode_captcha import CaptchaDecode

                c = CaptchaDecode()
                code, path = c.decode_response(response)
                self.decode_captcha(code)
                print("Try to decode:", code, path)

                return False, {"repeat": True}
            if errorCode == "404001":
                print("No information about phone in database")
            if errorCode == "403021":
                # Token dead
                Log.d("Token is dead.", config.TOKEN)
                self.updater.update_remain_count_by_token(config.TOKEN, 0)
        else:
            Log.d("Unhandled error with response", response)
            Log.d("Try to use correct token")
        return False, {}

    def send_req_to_the_server(self, url, payload, no_encryption=False):
        payload = self.prepare_payload(payload)
        self.headers["X-Req-Signature"] = self.cipher.create_signature(
            payload, self.timestamp
        )
        if no_encryption:
            is_ok, response = self.send_request_no_encrypted(url, payload)
        else:
            is_ok, response = self.send_request_encrypted(url, payload)

        if is_ok:
            # print(json.loads(self.cipher.decrypt_AES_b64(response)))
            return json.loads(self.cipher.decrypt_AES_b64(response))
        if not is_ok and "repeat" in response.keys() and response["repeat"]:
            return self.repeat_last_task()

        return response

    def repeat_last_task(self):
        function = self.current_task["function"]
        phone = self.current_task["phone"]

        if function == "get_phone_name":
            return self.get_phone_name(phone)
        if function == "get_phone_tags":
            return self.get_phone_tags(phone)

        Log.error("Incorrect task for repeat")
        return None

    def get_phone_name(self, phoneNumber):
        self.current_task = {"function": "get_phone_name", "phone": phoneNumber}
        self.update_config(config)
        method = "search"
        self.request_data["source"] = self.methods[method]
        self.request_data["phoneNumber"] = phoneNumber
        return self.send_req_to_the_server(
            self.base_url + self.base_uri_api + method, self.request_data
        )

    def get_phone_tags(self, phoneNumber):
        self.current_task = {"function": "get_phone_tags", "phone": phoneNumber}

        self.update_config(config)
        method = "number-detail"
        self.request_data["source"] = self.methods[method]
        self.request_data["phoneNumber"] = phoneNumber
        return self.send_req_to_the_server(
            self.base_url + self.base_uri_api + method, self.request_data
        )

    def decode_captcha(self, code):
        self.update_config(config)
        captcha_data = {"token": config.TOKEN, "validationCode": code}
        return self.send_req_to_the_server(
            self.base_url + self.base_uri_api + "verify-code", captcha_data
        )
