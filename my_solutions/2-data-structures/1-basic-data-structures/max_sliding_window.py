len1 = int(input())
arr = [int(x) for x in input().split()]
window_size = int(input())

max_index = -1
max_value = 0
for start in range(len1 - window_size + 1):
    end = start + window_size - 1
    if start <= max_index <= end:
        if arr[end] > max_value:
            max_value = arr[end]
            max_index = end
        print(max_value, end=' ')
    else:
        max_value = 0
        for i in range(start, end + 1):
            var = arr[i]
            if var > max_value:
                max_value = var
                max_index = i
        print(max_value, end=' ')

