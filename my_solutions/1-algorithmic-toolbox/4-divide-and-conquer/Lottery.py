def binary_search(arr, num, start, end):
    place = (end - start) // 2 + start
    if start > end:
        return end
    elif num == arr[place][1]:
        return place
    elif num > arr[place][1]:
        return binary_search(arr, num, place + 1, end)
    else:
        return binary_search(arr, num, start, place -1)


def wrap_binary(arr, num):
    return binary_search(arr, num, 0, len(arr) - 1)


def sum_influence(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i][0]
        arr[i][0] = sum


s, p = [int(x) for x in input().split()]
lines = []
for s in range(0, s):
    x = [int(x) for x in input().split()]
    lines.append([1, x[0]])
    lines.append([-1, x[1] + 1])
dots = [int(x) for x in input().split()]
lines.sort(key=lambda x: x[1])
sum_influence(lines)
s = ''
for dot in dots:
    s += str(lines[wrap_binary(lines, dot)][0]) + ' '
print(s)

