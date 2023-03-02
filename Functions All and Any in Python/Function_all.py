# Задача с канала: egoroff_channel
# 10.7 Функции all и any

# Программе на вход поступают слова, разделенные пробелом. Ваша задача проверить,
# во всех ли словах есть английская буква A вне зависимости от регистра.
# В качестве ответа программа должна вывести True или False.

#s = 'chase enlarge referee cup offense'
#s = 'acquaintance disAgree'
s = input()
ans = all(('a' in i.lower() for i in s.split()))
print(ans)