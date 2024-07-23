def custom_write(file_name, strings):
    string_number = 0
    strings_positions = {}
    for i in strings:
        f = open(file_name, 'a', encoding='utf-8')
        bytes_number = f.tell()
        string_number += 1
        f.write(i + "\n")
        f.close()
        key = (string_number, bytes_number)
        value = i
        strings_positions[key] = value

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
