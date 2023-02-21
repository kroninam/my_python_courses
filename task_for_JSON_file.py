# Задача с канала: egoroff_channel
# Решенная немного по-другому, чем в разборе на видео:
# https://www.youtube.com/watch?v=TzwS3VOZQvY

# Анализ продаж
# К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров.
# В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого автомобиля.
#
# Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж.
# В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.

import json
with open('manager_sales.json') as file:
    data = json.load(file)
for i in data:
    i['manager'].update({'sum_price': 0})

    for j in (i['cars']):
        i['manager']['sum_price'] += j['price']
prices = []
for i in data:
    prices.append(i['manager']['sum_price'])
for i in data:
    if i['manager']['sum_price'] == max(prices):
        print(i['manager']['first_name'], i['manager']['last_name'], i['manager']['sum_price'])