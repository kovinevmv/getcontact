import yaml
import os

from getcontact.config import config
from getcontact.logger import Log


class UpdateConfig:
    def __init__(self):
        self.config = config
        self.tokens_file = (
            os.path.dirname(
                os.path.abspath(__file__)) +
            "/../../dump/tokens.yaml")
        self.tokens_dict = self.read_yaml()
        self.update_status()

    def read_yaml(self):
        with open(self.tokens_file, "r") as f:
            data = yaml.safe_load(f.read())
            return data if data else {}

    def write_yaml(self, data):
        with open(self.tokens_file, "w") as f:
            f.write(yaml.dump(data, default_flow_style=False))

    def update_remain_count_by_token(self, token, remain_count):
        for values in self.tokens_dict.values():
            if values["TOKEN"] == token:
                values["REMAIN_COUNT"] = remain_count
        self.update_status()

    def decrease_remain_count_by_token(self, token):
        for values in self.tokens_dict.values():
            if values["TOKEN"] == token:
                values["REMAIN_COUNT"] -= 1
        self.update_status()

    def update_status(self):
        for values in self.tokens_dict.values():
            values["IS_ACTIVE"] = values["REMAIN_COUNT"] > 0
        self.save_dict()
        self.set_new_token(self.get_active())

    def save_dict(self):
        self.write_yaml(self.tokens_dict)

    def get_all_active(self):
        return list(
            filter(
                lambda x: x["IS_ACTIVE"], [
                    i[1] for i in self.tokens_dict.items()]))

    def get_any_active(self):
        tokens = self.get_all_active()
        if tokens:
            return tokens[0]

        Log.error("No valid token detected. Script will crash")
        return {}

    def get_new_active(self):
        current_token = self.config.TOKEN
        active = self.get_all_active()
        for values in active:
            if values["TOKEN"] != current_token:
                return values
        return None

    def get_active(self):
        active = self.get_all_active()
        return self.get_new_active() if len(active) >= 2 else self.get_any_active()

    def set_new_token(self, token):
        if "TOKEN" in token:
            self.config.TOKEN = token["TOKEN"]
            self.config.AES_KEY = token["AES_KEY"]
            self.config.ANDROID_OS = token["ANDROID_OS"]
            self.config.DEVICE_ID = token["DEVICE_ID"]

    def get_config(self):
        return self.config
