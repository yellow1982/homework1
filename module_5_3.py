class Building:
    total = 0

    def __init__(self):
        Building.total += 1


while Building.total < 40:
    name_bilding = "bild_" + str(Building.total)
    name_bilding = Building()
    print(name_bilding)

