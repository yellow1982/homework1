import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        count_of_enemies = 100
        day_number = 1
        print(f"{self.name}, на нас напали!")
        while count_of_enemies > 0:
            count_of_enemies -= self.power
            print(f"{self.name} сражается {day_number} день(дней), осталось {count_of_enemies} воинов.")
            time.sleep(1)
            day_number += 1
        print(f"{self.name} одержал победу спустя {day_number - 1} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончилиись!")