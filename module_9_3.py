first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(key) - len(value) for key, value in zip(first, second) if len(key) != len(value))
second_result = ((len(x) == len(y)) for x in first for y in second if first.index(x) == second.index(y))

print(list(first_result))
print(list(second_result))
