grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
students_dict = {}
for x in grades:
    summa = 0
    for y in grades[grades.index(x)]:
        summa += y
    students_dict[students_list[grades.index(x)]] = summa / len(grades[grades.index(x)])
print(students_dict)
