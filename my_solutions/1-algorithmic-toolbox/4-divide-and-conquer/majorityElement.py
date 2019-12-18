n = int(input())
arr = [int(x) for x in input().split()]
def count(arr, var, start, end):
    count = 0
    for i in range(start, end + 1):
        if arr[i] == var:
            count += 1
    return count



def majority(arr, start, end):
    if start + 1 == end:
        if arr[start] == arr[end]:
            return arr[start]
        else:
            return -1
    if start == end:
        return arr[start]
    list1 = [start, (end - start) // 2 + start]
    list2 = [(end - start) // 2 + 1 + start, end]
    ret1 = majority(arr, *list1)
    ret2 = majority(arr, *list2)
    if ret1 == ret2:
        return ret1
    else:
        count1 = count(arr, ret1, *list2)
        count2 = count(arr, ret2, *list1)
        if count1 > count2:
            return ret1
        elif count2 > count1:
            return ret2
        else:
            return ret1


if majority(arr, 0, n - 1) != -1:
    print(1)
else:
    print(0)

