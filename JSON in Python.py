# Задача с канала: egoroff_channel
#9.3 Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
# https://www.youtube.com/watch?v=SdXGg-jw9gs

# В json-файле содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор.
#
# Ваша задача скачать файлик и самостоятельно найти идентификатор группы, в которой находится самое большое
# количество женщин, рожденных после 1977 года. В качестве ответа необходимо указать через пробел идентификатор
# найденной группы и сколько в ней было женщин, рожденных после 1977 года.


import json

with open ('group_people.json') as file:
    file = json.load(file)
d = {}
for i in file:
    for j in i['people']:
        if int(j['year']) > 1977 and j['gender'] == 'Female':
            d.setdefault(i['id_group'],0)
            d[i['id_group']] += 1

print(d)
maxi = 0
for value in d.values():
    if value > maxi:
        maxi = value

for k, w in d.items():
    if w == maxi:
        print(k,w)

