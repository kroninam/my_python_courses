# Задача с канала: egoroff_channel
#10.4 Функция zip

# Перед вами два списка одинаковой длины keys и values
#
# Ваша задача создать словарь result, в котором пара
# ключ-значение берется из значений списков, стоящих на одинаковых индексах.
# В качестве ответа выведите словарь result

keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = dict(zip(keys, values))
print(result)