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