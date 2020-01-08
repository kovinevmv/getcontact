import base64
import codecs
import hashlib
import hmac
from Crypto.Cipher import AES

from getcontact.config import config


class Cipher:
    def __init__(self, config_=None):
        self.update_config(config_)
        self.BS = 16

    def update_config(self, config_):
        self.config = config_ if config_ else config
        self.update_cipher()

    def update_cipher(self):
        self.cipher_aes = AES.new(codecs.decode(self.config.AES_KEY, 'hex'), AES.MODE_ECB)

    def pad_data(self, s):
        return bytes(s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS), 'utf8')

    def unpad_data(self, s):
        return s[0:-ord(s[-1])]

    def calculate_new_aes_key_by_server(self, server_key):
        key = int(server_key) ** self.config.PRIVATE_KEY % self.config.MOD_EXP
        new_key = hashlib.sha256(bytearray(str(key), "utf-8")).hexdigest()
        return str(new_key)

    def create_signature(self, payload, timestamp):
        message = bytes(self.format_message_to_hmac(payload, timestamp), 'utf8')
        secret = bytes(self.config.HMAC_KEY, 'utf8')
        signature = self.encode_b64(hmac.new(secret, msg=message, digestmod=hashlib.sha256).digest())
        return signature

    def format_message_to_hmac(self, msg, timestamp):
        return f"{timestamp}-{msg}"

    def encode_b64(self, data):
        return base64.b64encode(data)

    def decode_b64(self, data):
        return base64.b64decode(data)

    def decrypt_AES(self, data):
        return self.unpad_data(self.cipher_aes.decrypt(data).decode())

    def encrypt_AES(self, data):
        return self.cipher_aes.encrypt(self.pad_data(data))

    def encrypt_AES_b64(self, data):
        return self.encode_b64(self.encrypt_AES(data)).decode()

    def decrypt_AES_b64(self, data):
        return self.decrypt_AES(self.decode_b64(data))


if __name__ == "__main__":
    pass
