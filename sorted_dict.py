# Сортировка коллекций. Сортировка словаря.
# Напишите программу, которая отсортирует список models по цвету в лексикографическом порядке (по алфавиту).
# Затем распечатайте элементы этого списка, каждый элемент на новой строке в формате:
# Производитель: <make>, модель: <model>, цвет: <color>

models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
a = sorted(models, key=lambda x: x['color'])
for i in a:
    print(f'Производитель: {i["make"]}, модель: {i["model"]}, цвет: {i["color"]}')





