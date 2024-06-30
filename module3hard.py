def calculate_structure_sum(data):
    sum_ = 0
    if isinstance(data, (int, float)):
        sum_ += data
    elif isinstance(data, str):
        sum_ += len(data)
    elif isinstance(data, (list, set, tuple)):
        for i in data:
            sum_ += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)

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
