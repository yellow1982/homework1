import threading


class BankAccount:
    balance = 1000
    lock_1 = threading.Lock()
    lock_2 = threading.Lock()

    def deposit(self, amount):
        try:
            self.lock_1.acquire()
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")
        finally:
            self.lock_1.release()

    def withdraw(self, amount):
        try:
            self.lock_2.acquire()
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")
        finally:
            self.lock_2.release()

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
