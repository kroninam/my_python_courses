# Задача с канала: egoroff_channel
#10.4 Функция filter

# Напишите программу, которая отфильтрует список days так,
# чтобы в нем остались только дни, названия которых состоят из
# четырех символов или начинаются с буквы S. Используйте при этом lambda функцию.
#
# Распечатайте получившийся список в алфавитном порядке, каждый элемент на новой строчке/

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

ans = list(filter(lambda x: len(x) == 4 or x[0] == 'S', days))

for i in sorted(ans):
    print(i)