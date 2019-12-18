def binary_search(arr, num, start, end):
    place = (end - start) // 2 + start
    if start > end:
        return -1
    elif num == arr[place]:
        return place
    elif num > arr[place]:
        return binary_search(arr, num, place + 1, end)
    else:
        return binary_search(arr, num, start, place -1)

def wrap_binary(arr, num):
    return binary_search(arr, num, 0, len(arr) - 1)

n, *arr = [int(x) for x in input().split()]
k, *search = [int(x) for x in input().split()]
results = ''
results += str(wrap_binary(arr, search[0]))
for number in search[1:]:
    results += " " + str(wrap_binary(arr, number))
print(results)

