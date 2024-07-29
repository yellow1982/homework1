from datetime import datetime
from threading import Thread
import time


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово №{i}\n")
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_stop = datetime.now()
print(f"Работа потоков {time_stop - time_start}")

thread_one = Thread(target=write_words, args=(10, "example5.txt"))
thread_two = Thread(target=write_words, args=(30, "example6.txt"))
thread_three = Thread(target=write_words, args=(200, "example7.txt"))
thread_four = Thread(target=write_words, args=(100, "example8.txt"))
time_start = datetime.now()
thread_one.start()
thread_two.start()
thread_three.start()
thread_four.start()

thread_one.join()
thread_two.join()
thread_three.join()
thread_four.join()
time_stop = datetime.now()
print(f"Работа потоков {time_stop - time_start}")