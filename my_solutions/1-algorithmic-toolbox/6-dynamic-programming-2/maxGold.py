max_capacity2, len1 = [int(x) for x in input().split()]

gold_array = [int(x) for x in input().split()]

hash_table = {}

def max_value(max_capacity, gold_array, i):
    if i == - 1:
        return 0
    options = []
    if hash_table.get((max_capacity, i)) is not None:
        return hash_table[(max_capacity, i)]
    if gold_array[i] <= max_capacity:
        options.append(max_value(max_capacity - gold_array[i], gold_array, i - 1) + gold_array[i])
    options.append(max_value(max_capacity, gold_array, i - 1))
    hash_table[(max_capacity, i)] = max(options)
    return hash_table[(max_capacity, i)]

print(max_value(max_capacity2, gold_array, len(gold_array) - 1))
