import os

from PIL import Image, ImageEnhance


def new_image(name):
    image = Image.open(name)
    w, h = image.size                   # объявляем переменные, записываем в них высоту и ширину
    image.resize((w // 3, h // 3))      # уменьшаем изображение в три раза
    enh = ImageEnhance.Contrast(image)  # объявляем переменную и присваиваем ей значение контраста изображения
    enh.enhance(1.8).show()             # увеличиваем контраст на 80 процентов и выводим полученное изображение на экран
    f, e = os.path.splitext(name)       # делим название файла на имя и расширение
    image.save(f + '.png')              # сохраняем файл с новым расширением


im = new_image('Photo.jpg')