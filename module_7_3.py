class WordsFinder:
    file_names = []

    def __init__(self, *file_name):
        for file in file_name:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                words = f.read().replace('\n', ' ')
                symbols_for_remove = (',', '.', '=', '!', '?', ';', ':', ' - ')
                words = ''.join(c for c in words if c not in symbols_for_remove).lower().split()

                all_words[file] = words
                return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            place = 0
            for i in words:
                place += 1
                if word.lower() == i.lower():
                    find_dict[name] = place
                    break
        return find_dict

    def count(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            count_of_words = 0
            for i in words:
                if word.lower() == i.lower():
                    count_of_words += 1
                    find_dict[name] = count_of_words
        return find_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))
