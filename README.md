## About

This project allows you to get some information about person by his phone number. 


After decompiling the application [GetContact](https://www.getcontact.com/ru/), I created simple API to get information directly without installing this application. Unfortunately, the application sends your contacts from the smartphone notebook to public database, but this problem does not occur using this script :)

## How to get keys

If script doens't run properly try to update token\`s inforamation in `dump/tokens.yaml` file. Or if you want to run with Premium Account enter your auth data in this file. 

Requirements: Android with ROOT-rights.

Open in filemanager of phone ` /data/data/app.source.getcontact/shared_prefs/GetContactSettingsPref.xml` 

* AES key: `FINAL_KEY`
* token: `TOKEN`
* exp: `PRIVATE_KEY`


## How to run 
### Python3

- Create and run venv
```shell script
[ ! -d venv ] && python3 -m venv venv; source venv/bin/activate
```

- Install requirements
```shell script
pip3 install -r requirements.txt
```

- Console output
```shell script
python3 ./src/main.py -p +79291045342
```
Output:
```
Phone: +79291045342
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

- Console JSON-format output 
```shell script
python3 ./src/main.py -j -p +79291045342
```
Output:
```json5
{'name': None, 'phoneNumber': '+79291045342', 'country': 'RU', 'displayName': 'Андрей Тимофеев', 'profileImage': None, 'email': None, 'is_spam': False, 'remain_count': 194, 'tags': ['Андрей Тимофеев', 'Андрей Спб', 'Андрей Челентос', 'Андрей Катин', 'Андрей', 'Онлрей', 'Экс Бойфренд Aka Реальный Долбоеб', 'Андрей Chelentos', 'Andrey Tymofeev', 'Андрей Тим', 'Андрюша :', 'Андрей 💑', '.andrey', 'Andrey']}
```


### Docker
```shell script
chmod +x ./run.sh
sudo docker build . -t getcontact
sudo docker run -t getcontact -p +79291045342
```
