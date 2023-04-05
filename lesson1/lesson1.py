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
