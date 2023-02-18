#Интересные и полезные вещи:


#1.
# интересный генератор списков:
[i.split(':') for i in iter(input, 'конец')]
#iter здесь принимает функцию и стоп-значение.
# Функция будет выполняться, пока не вернёт стоп значение.
# Некий аналог цикла while


#2.
# обычный генератор списковЖ
num = int(input())
names_list = [input() for i in range (num)]
print(names_list)

#3.
# генератор таблицы

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range (n)]

for i in a:
    print(i)

# Sample input
# 2 3
# 1 2 3
# 4 5 6


# словарь через if-else:
with open (file_name, 'r') as file:
    words = {}
    for i in file.readlines():
        #print (i.strip())
        for j in i.strip().split():
            #print(j)
            if j.upper() not in words:
                words[j.upper()] = 1
            elif j.upper() in words:
                words[j.upper()] += 1
print(words)

# методы словаря:
#setdefault
for word in [какой-нибудь список]:
        words.setdefault(word, 0)
        words[word] += 1

#get
words[word]  =  words.get(word, 0) + 1



