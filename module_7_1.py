from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name, 'r')
        return f.read()

    def add(self, *products):
        prod_in_list = True
        for i in products:
            print("i.name = ", i.name)
            if not self.get_products().splitlines():
                print("пустой список, делаем первую запись", i)
                f = open(self.__file_name, 'a')
                f.write(f'{i}\n')
                print("Добавился в список", self.get_products().splitlines())
                f.close()
            for j in self.get_products().splitlines():
                print("j = ", j, "i.name = ", i.name)
                if j.startswith(i.name):
                    prod_in_list = True
                    print(f"Продукт {i.name} уже есть в магазине")
                    break
                else:
                    prod_in_list = False
            if not prod_in_list:
                f = open(self.__file_name, 'a')
                f.write(f'{i}\n')
                print("Добавился в список", self.get_products().splitlines())
                f.close()
                break


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
