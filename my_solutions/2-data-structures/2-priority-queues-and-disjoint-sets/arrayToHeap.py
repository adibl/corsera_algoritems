arr_len = int(input())
arr = [int(x) for x in input().split()]


def move_min(arr, i):
    child1 = 2 * i + 1
    child2 = 2 * i + 2
    if  child1 < len(arr) and child2 < len(arr):
        if arr[child1] > arr[child2]:
            min_child_index = child2
        else:
            min_child_index = child1
        if arr[i] > min(arr[child1], arr[child2]):
            arr[i], arr[min_child_index] = arr[min_child_index], arr[i]
            return min_child_index
        else:
            return i
    elif child1 < len(arr) and child2 >= len(arr):
        if arr[child1] < arr[i]:
            arr[i], arr[child1] = arr[child1], arr[i]
            return child1
        else:
            return i
    elif child1 >= len(arr) and child2 < len(arr):
        if arr[child2] < arr[i]:
            arr[i], arr[child2] = arr[child2], arr[i]
            return child2
        else:
            return i
    else:
        return i


#import pdb;pdb.set_trace()
count = 0
s = ''
for i in range(arr_len - 1, -1, -1):
    index_to_move = move_min(arr, i)
    while i != index_to_move:
        s += str(i) + ' ' + str(index_to_move) + '\n'
        count += 1
        i = index_to_move
        index_to_move = move_min(arr, i)
print(count)
print(s)
