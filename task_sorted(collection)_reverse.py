# Сортировка коллекций
#
# Напишите программу, которая отсортирует список subject_marks по убыванию оценок.
#
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел.
#
#

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
def key(x):
    return x[1]

subject_marks_sorted = sorted(subject_marks, key = key, reverse=True)

for i in subject_marks_sorted:
    print(*i)