import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()



    def process_request(self, request):
        if request[1] == "receipt":
            self.data[request[0]] = request[2]

        if request[1] == "shipment":
            for item in self.data.items():
                if item[0] == request[0]:
                    self.data[item[0]] = item[1] - request[2]


    def run(self, requests):
        with multiprocessing.Pool(processes=1) as pool:
            pool.map(self.process_request, requests)


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
