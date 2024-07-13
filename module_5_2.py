class House:
    def __init__(self):
        self.number_of_floors = 0

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        print(f"Number of floors: {self.number_of_floors}")


h1 = House()
h2 = House()
h1.setNewNumberOfFloors(10)
h2.setNewNumberOfFloors(4)

