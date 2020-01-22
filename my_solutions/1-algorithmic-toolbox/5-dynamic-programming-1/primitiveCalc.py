n = int(input())
arr = [[0, 0]]
operations = []
number = 1
for number in range(2, n + 1):
    options = []
    if number // 3 == number / 3:
        var = arr[number // 3 - 1]
        options.append([var[0] + 1, 3])
    if number // 2 == number / 2:
        var = arr[number // 2 - 1]
        options.append([var[0] + 1, 2])
    options.append([arr[-1][0] + 1, 1])
    options.sort(key=lambda x: x[0])
    arr.append(options[0])
s = str(arr[n - 1][0]) + '\n'
operators = [x[1] for x in arr]
i = len(operators)
numbers = [n]
while i > 1:
    if operators[i - 1] == 3 or operators[i - 1] == 2:
        numbers.append(numbers[-1] // operators[i - 1])
        i = i // operators[i - 1]
    elif operators[i - 1] == 1:
        i = i - 1
        numbers.append(numbers[-1] - 1)
s += " ".join(str(x) for x in numbers[::-1])
print(s)
print(s2)
