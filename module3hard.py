def calculate_structure_sum(data):
    sum_ = 0
    if len(data) == 0:
        return sum_
    first = data[0]
    if len(data) == 1:
        if isinstance(first, int):
            sum_ += first
        elif isinstance(first, str):
            sum_ += len(first)
        elif isinstance(first, tuple):
            sum_ += calculate_structure_sum(list(first))
        elif isinstance(first, list):
            sum_ += calculate_structure_sum(first)
        elif isinstance(first, dict):
            sum_ += calculate_structure_sum(list(first.items()))
        elif isinstance(first, set):
            sum_ += calculate_structure_sum(list(first))
        return sum_
    elif len(data) > 1:
        if isinstance(first, int):
            sum_ += first + calculate_structure_sum(data[1:])
        elif isinstance(first, str):
            sum_ += len(first) + calculate_structure_sum(data[1:])
        elif isinstance(first, tuple):
            sum_ += calculate_structure_sum(list(first)) + calculate_structure_sum(data[1:])
        elif isinstance(first, list):
            sum_ += calculate_structure_sum(first) + calculate_structure_sum(data[1:])
        elif isinstance(first, dict):
            sum_ += calculate_structure_sum(list(first.items())) + calculate_structure_sum(data[1:])
        elif isinstance(first, set):
            sum_ += calculate_structure_sum(list(first)) + calculate_structure_sum(data[1:])
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
