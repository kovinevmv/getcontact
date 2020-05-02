from getcontact.config import config
from getcontact.config_updater import UpdateConfig
from getcontact.requester import Requester


def parse_none(data):
    return '' if data is None else data


class GetContactAPI:
    def __init__(self):
        self.updater = UpdateConfig()
        self.requester = Requester(self.updater.get_config())

    def get_name_by_phone(self, phoneNumber):
        response = self.requester.get_phone_name(phoneNumber)
        if response:
            name = response['result']['profile']['name']
            surname = response['result']['profile']['surname']
            if not name and not surname:
                user_name = None
            else:
                user_name = f'{parse_none(name)} {parse_none(surname)}'

            country_code = response['result']['profile']['countryCode']
            country = response['result']['profile']['country']

            if not country:
                country_name = f"{parse_none(country_code)}"
            else:
                country_name = f'{country} {parse_none(country_code)}'

            result = {"name": user_name,
                      "phoneNumber": response['result']['profile']['phoneNumber'],
                      "country": country_name,
                      "displayName": response['result']['profile']['displayName'],
                      "profileImage": response['result']['profile']['profileImage'],
                      "email": response['result']['profile']['email'],
                      "is_spam": True if response['result']['spamInfo']["degree"] == "high" else False}

            remain_count = response['result']['subscriptionInfo']['usage']['search']['remainingCount']
            self.updater.update_remain_count_by_token(config.TOKEN, remain_count)

            return result
        else:
            return {"name": None,
                    "phoneNumber": phoneNumber,
                    "country": config.COUNTRY,
                    "displayName": "Not Found",
                    "profileImage": None,
                    "email": None,
                    "is_spam": False}

    def get_tags_by_phone(self, phoneNumber):
        response = self.requester.get_phone_tags(phoneNumber)
        if response:
            result = {"tags": [tag['tag'] for tag in response['result']['tags']]}
            return result
        else:
            return {"tags": []}

    def update_config(self):
        self.requester.update_config(self.updater.get_config())

    def get_name_by_phone_with_change_token(self, phone):
        result = self.get_name_by_phone(phone)
        self.update_config()
        return result

    def get_information_by_phone(self, phone):
        result_name = self.get_name_by_phone(phone)
        result_tags = self.get_tags_by_phone(phone)

        self.update_config()

        return dict(**result_name, **result_tags)

    def print_information_by_phone(self, phone):
        data = self.get_information_by_phone(phone)
        self._print_beauty_output(data)

    def get_from_file(self, file):
        phones = open(file, 'r').read().split('\n')
        for phone in phones:
            self.print_information_by_phone(phone)

    def _print_beauty_output(self, data):
        print("Phone:", data['phoneNumber'])
        print("User:", data['displayName'])
        if 'tags' in data.keys() and data['tags']:
            print('Tag list: ')
            for tag in data['tags']:
                print("\t", tag.encode('utf-8', errors='replace').decode('utf-8', errors='replace'))
