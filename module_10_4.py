from queue import Queue
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number: int):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.q = Queue()
        self.list_of_customers = []


    def customer_arrival(self):
        customer = 1
        max_customers = 20
        cafe_is_closed = False
        while True:
            if cafe_is_closed:
                break
            print(f"Посетитель номер {customer} прибыл.")
            if (table1.is_busy and table2.is_busy and table3.is_busy) and self.q.empty():
                print(f"Посетитель номер {customer} ожидает свободный стол.")
                self.q.put(customer)
                sleep(1)
                customer += 1
                continue
            if not self.q.empty():
                print(f"Посетитель номер {customer} ожидает свободный стол.")
                self.q.put(customer)
            if not table1.is_busy or not table2.is_busy or not table3.is_busy:
                if self.q.empty():
                    self.serve_customer(customer)
                else:
                    self.serve_customer(self.q.get())
            sleep(0.1)
            customer += 1

            if customer > max_customers:
                while True:
                    if not table1.is_busy or not table2.is_busy or not table3.is_busy:
                        self.serve_customer(self.q.get())
                        if self.q.empty():
                            cafe_is_closed = True
                            break

    def serve_customer(self, customer):
        for table in tables:
            if not table.is_busy:
                new_cust = Customer(customer, table)
                new_cust.start()
                break


class Customer(Thread):
    def __init__(self, customer, table):
        super().__init__()
        self.customer = customer
        self.table = table

    def run(self):
        self.table.is_busy = True
        print(f"Посетитель номер {self.customer} сел за стол номер {self.table.number}.")
        sleep(5)
        print(f"Посетитель номер {self.customer} покушал и ушел.")
        self.table.is_busy = False


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()

customer_arrival_thread.join()
