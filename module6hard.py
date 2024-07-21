import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False

        #если передать только один размер для фигуры, то фигура будет считаться равносторонней
        default_sides = []
        if len(sides) == 1 and sides[0] > 0 and isinstance(sides[0], int):
            for i in range(self.sides_count):
                default_sides.append(sides[0])
            self.__sides = list(default_sides)

        if self.__is_valid_sides(*sides):
            self.__sides = sides
        else:
            if not default_sides:
                for i in range(self.sides_count):
                    default_sides.append(1)
                self.__sides = list(default_sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b,
                                                                    int) and 0 <= r < 256 and 0 <= g < 256 and 0 <= b < 256:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for i in sides:
            if i < 0 or not isinstance(i, int):
                return False
        if len(sides) == self.sides_count:
            return True
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def get_sides(self):
        list_of_sides = list(self.__sides)
        return list_of_sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = int(self.get_sides()[0]) / (2 * math.pi)

    def get_square(self):
        return math.pi * math.sqrt(self.__radius)


class Triangle(Figure):  # По заданию, судя по всему, треугольник должен быть равносторонним. Я заморочился,
                        # сделал код для любого возможного треугольника
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if not self.triangle_is_possible():
            super().__init__(color, 1, 1, 1)
        self.height = 2 * self.get_square() / self.get_sides()[0]

    # Проверка на возможность существования треугольника
    def triangle_is_possible(self):
        global pos_tri  # Сделал переменную глобальной, чтоб не повторять длинный код для вычисления площади
        pos_tri = (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]) / 2 * ((self.get_sides()[0] +
                                                                                            self.get_sides()[1] +
                                                                                            self.get_sides()[2]) / 2 -
                                                                                           self.get_sides()[0]) * (
                              (self.get_sides()[0] +
                               self.get_sides()[1] + self.get_sides()[2]) / 2 - self.get_sides()[1]) * (
                              (self.get_sides()[0] +
                               self.get_sides()[1] + self.get_sides()[2]) / 2 - self.get_sides()[2])
        if pos_tri > 0:
            return True
        else:
            return False

    def get_square(self):
        if self.triangle_is_possible():
            return math.sqrt(pos_tri) #Здесь использовал глобальную переменную


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        new_sides = sides[0] # Программа будет работать и без этого кода, но останется возможность сосздать куб с 12
                            # разными сторонами, поэтому этот код, чтоб исключить такую возможность
        super().__init__(color, new_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
