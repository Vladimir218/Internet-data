# Task1
# Посмотреть документацию к API GitHub,
# разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json
import os
from pathlib import Path

url = 'https://api.github.com'
username='Vladimir218'

r = requests.get(f'{url}/users/{username}/repos')

with open('Internet-data/Internet-data/lesson1/task1.json', 'w') as f:
    json.dump(r.json(), f)


for i in r.json():
    print(f"{i['id']} {i['name']}")


# Task2
# Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
# Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему,
# пройдя авторизацию. Ответ сервера записать в файл.
# Если нет желания заморачиваться с поиском, возьмите API вконтакте
# (https://vk.com/dev/first_guide). Сделайте запрос, чтобы получить
# список всех сообществ на которые вы подписаны.


url = 'https://api.github.com/user/emails'
token = input('Введите токен доступа: ')

headers = {
    'Authorization': f'Bearer {token}'
}

email_information = requests.get(f'{url}', headers = headers)
print(email_information.json())

with open('Internet-data/Internet-data/lesson1/task2.json', 'w') as f:
    json.dump(email_information.json(), f)
