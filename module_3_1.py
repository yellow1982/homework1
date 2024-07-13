calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_):
    count_calls()
    return len(str_), str_.upper(), str_.lower()


def is_contains(str_, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() is str_.lower():
            return True
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
