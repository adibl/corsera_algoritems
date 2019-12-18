def marge(arr1, arr2):
    result = []
    count = 0
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            count += len(arr1) - i
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result, count


def marge_sort(arr):
    total_count = 0
    if len(arr) == 1:
        return arr, 0
    mid = len(arr) // 2
    arr1, count = marge_sort(arr[:mid])
    total_count += count
    arr2, count = marge_sort(arr[mid:])
    total_count += count
    arr, count = marge(arr1, arr2)
    total_count += count
    return arr, total_count

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    result, count = marge_sort(arr)
    print(count)