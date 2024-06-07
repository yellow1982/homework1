def single_root_words(root_word, *other_words):
    other = []
    for i in other_words:
        other.append(i)
    same_words = []
    for word in other:
        if word.lower().count(root_word.lower()) or root_word.lower().count(word.lower()):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
