# Сортировка коллекций
# Напишите программу, которая отсортирует список subject_marks по возрастаю оценок.
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]


def key(x):
    return x[1]


a = sorted(subject_marks, key=key)

for i in a:
    print(*i)