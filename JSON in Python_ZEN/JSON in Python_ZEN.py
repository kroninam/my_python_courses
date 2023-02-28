# Задача с канала: egoroff_channel
# Задание 9.3 Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
# В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле.
# Ключ для декодирования располагается в json-файле. В качестве ответа нужно просто отправить
# получившийся текст.  И обратите внимание, что раскодировать нужно только лишь буквы,
# все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.
# Сами файлы здесь же добавил.
import json

with open ('Abracadabra__1_.txt') as file:
    file = file.read()
    #print(file)

with open ('Alphabet.json') as file1:
    data = json.load(file1)
    #print(data)

answer = ''
for i in file:
    if i in data:
        i = data[i]
        answer += i
    else:
        answer += i
print(answer)