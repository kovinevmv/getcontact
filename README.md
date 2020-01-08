## How to get keys

Open ` /data/data/app.source.getcontact/shared_prefs/GetContactSettingsPref.xml` 

* AES key: `FINAL_KEY`
* token: `TOKEN`
* exp: `PRIVATE_KEY`


## How to run 

Console output
```bash
python3 ./src/main.py -p +79291045342
```
Output:
```bash
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

Console JSON-format output 
```bash
python3 ./src/main.py -j -p +79291045342
```
Output:
```bash
{'name': None, 'phoneNumber': '+79291045342', 'country': 'RU', 'displayName': 'Андрей Тимофеев', 'profileImage': None, 'email': None, 'is_spam': False, 'remain_count': 194, 'tags': ['Андрей Тимофеев', 'Андрей Спб', 'Андрей Челентос', 'Андрей Катин', 'Андрей', 'Онлрей', 'Экс Бойфренд Aka Реальный Долбоеб', 'Андрей Chelentos', 'Andrey Tymofeev', 'Андрей Тим', 'Андрюша :', 'Андрей 💑', '.andrey', 'Andrey']}
```