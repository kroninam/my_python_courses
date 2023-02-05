# Напишите программу, которая отсортирует список subject_marks по убыванию оценок.
# Предметы, имеющих одинаковые оценки, должны быть отсортированы в алфавитном порядке
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел.

subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

s_m_sorted = sorted(subject_marks, key = lambda x: (-int(x[1]), x[0]))

for i in s_m_sorted:
    print(*i)

# print(subject_marks[0][0])