[![Codacy Badge](https://api.codacy.com/project/badge/Grade/433da7bd8f1f4eddaf339aeb30989e18)](https://app.codacy.com/manual/kovinevmv/getcontact?utm_source=github.com&utm_medium=referral&utm_content=kovinevmv/getcontact&utm_campaign=Badge_Grade_Dashboard)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/kovinevmv/getcontact.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kovinevmv/getcontact/context:python)

## Update [01.01.2022]

- GetContact changed API, therefore **project is not working**. Maybe in future will be fixed

## Update [01.02.2021]

- Captcha not working in GetContact App, therefore my scripts doesn't pass verification too :( Please, use another tokens

## Warning 

This project is not intended for downloading GetContact database. This project provides the opportunity to receive information by phone number **with a limited number of requests for one token per month**. Several examples of tokens are posted in the repository.
**If the script does not work, use your tokens, run script in debug mode**

## About

After decompiling the application [GetContact](https://www.getcontact.com/ru/), I created simple API to get information directly without installing this application. Unfortunately, the application sends your contacts from the smartphone notebook to public database, but this problem does not occur using this script :)

## How to get keys

If script doesn't run properly try to update token\`s inforamation in `dump/tokens.yaml` file. Or if you want to run with Premium Account enter your auth data in this file. 

Requirements: Android with ROOT-rights (or emulator).

Open in filemanager of phone ` /data/data/app.source.getcontact/shared_prefs/GetContactSettingsPref.xml` 

  * AES key: `FINAL_KEY`
  * token: `TOKEN`

Edit `dump/tokens.yaml` with your data by:
  * `AES_KEY`: AES key from `GetContactSettingsPref.xml` 
  * `ANDROID_OS`: For example `android 5.0`
  * `DEVICE_ID`: For example `14130e29cebe9c39`
  * `IS_ACTIVE`: `true` if your token is valid
  * `REMAIN_COUNT`: Any natural num if your token is valid
  * `TOKEN`: token from `GetContactSettingsPref.xml`

## How to run 

Install [tesseract](https://github.com/tesseract-ocr/tesseract/wiki) to bypass captcha

### Python3

#### Create and run venv
```shell script
[ ! -d venv ] && python3 -m venv venv; source venv/bin/activate
```

#### Install requirements
```shell script
pip3 install -r requirements.txt
```

#### Console output
```shell script
python3 ./src/main.py -p +792910453XX
```
Output:
```
Phone: +792910453XX
User: Андрей Тимофеев
Tag list: 
	 Андрей Тимофеев
	 Андрей Спб
	 Андрей Челентос
	 Андрей Катин
	 Андрей
	 Онлрей
	 Экс Бойфренд Aka Реальный Долбоеб
	 Андрей Chelentos
	 Andrey Tymofeev
	 Андрей Тим
	 Андрюша :
	 Андрей 💑
	 .andrey
	 Andrey
Remain count: 194
```

#### Console JSON-format output 
```shell script
python3 ./src/main.py -j -p +792910453XX
```
Output:
```json5
{'name': None, 'phoneNumber': '+792910453XX', 'country': 'RU', 'displayName': 'Андрей Тимофеев', 'profileImage': None, 'email': None, 'is_spam': False, 'remain_count': 194, 'tags': ['Андрей Тимофеев', 'Андрей Спб', 'Андрей Челентос', 'Андрей Катин', 'Андрей', 'Онлрей', 'Экс Бойфренд Aka Реальный Долбоеб', 'Андрей Chelentos', 'Andrey Tymofeev', 'Андрей Тим', 'Андрюша :', 'Андрей 💑', '.andrey', 'Andrey']}
```

#### Debug mode
```shell script
python3 ./src/main.py -v -p +792910453XX
```
Output:
```
[2020-08-09 21:19:30] Call print_information_by_phone with phone  +792910453XX
[2020-08-09 21:19:30] Call get_information_by_phone with phone  +792910453XX
[2020-08-09 21:19:30] Call get_name_by_phone with phoneNumber  +792910453XX
[2020-08-09 21:19:30] Call _send_post with url: https://pbssrv-centralevents.com/v2.5/search data: {"data": "IntagsrX4IGrPHP7pfJfl9jBqULuZK25pFdPYdCGjSEovlUiPr9rdM/O1rcOcW6WPKUONujPcQKWBlEVzv5R6sFelyff9c5su48kI6fqBZpjVGohthrvzOKtuCC0Tne9N1v30b0PL4HKQrmWPlik8kGCSqajsivlJ01a+e9ELkXk/AjaHrm9cZVxyCfZpx4D"}
...
'Try premium free', 'subsInfoButtonIntroText': 'Try Getcontact Premium now to increase tag view limit and enjoy other Premium Benefits.'}}}
[2020-08-09 21:19:31] Call _print_beauty_output with data  {'name': None, 'phoneNumber': '+792910453XX', 'country': 'RU', 'displayName': 'Not Found', 'profileImage': None, 'email': None, 'is_spam': False, 'tags': []}
Phone: +792910453XX
User: Not Found
```



### Docker
```shell script
chmod +x ./run.sh
sudo docker build . -t getcontact
sudo docker run -t getcontact -p +792910453XX
```
