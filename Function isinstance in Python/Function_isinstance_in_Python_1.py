# Задача с канала: egoroff_channel
# 10.6 Встроенная функция isinstance

# Ваша задача написать функцию count_strings, которая принимает произвольное количество аргументов.
# Функция должна среди всех переданных значений найти только строки, найти их количество и
# вернуть в качестве результата.
#
# Ниже представлены примеры:
#
# count_strings(1, 2, 'hello', [2, 3, 4], True) => 1
# count_strings('am', 'world', 'hello', 'is') => 4
# count_strings() => 0
# count_strings(True, False) => 0


def count_strings(*args):
    count = 0
    for i in (args):
        if isinstance(i, str):
            count +=1
    return count

print(count_strings(1, 2, 'hello', [2, 3, 4], True))
print(count_strings('am', 'world', 'hello', 'is'))
print(count_strings())
print(count_strings(True, False))