my_dict = {"Иван": 1987, "Владимир": 1976, "Сергей": 1994, "Марина": 2001}
print("Словарь:", my_dict)
print("Существующее значение:", my_dict.get("Марина"))
print("Несуществующее значение:", my_dict.get("Елена"))
my_dict.update({"Вероника": 2005, "Дарья": 1987})
print("Удаленное значение:", my_dict.pop("Иван"))
print("Измененный словарь:", my_dict)
print("")
my_set = {1, 2, 3, "Строка", 2, 3, 5}
print("Множество:", my_set)
my_set.add(7)
my_set.add(10)
my_set.discard(1)
print("Измененное множество:", my_set)
