import random


def partition(arr, start, end):
    partitiona = random.randint(start, end - 1)
    arr[start], arr[partitiona] = arr[partitiona], arr[start]
    m1, m2 = start, start
    for i in range(start + 1, end):
        if arr[i] < arr[m1]:
            m2 += 1
            arr[i], arr[m2] = arr[m2], arr[i]
            arr[m1], arr[m2] = arr[m2], arr[m1]
            m1 += 1
        elif arr[i] == arr[m1]:
            m2 += 1
            arr[m2], arr[i] = arr[i], arr[m2]
    return m1, m2


def quick_sort(arr, start, end):
    while start < end - 1:
        m1, m2 = partition(arr, start, end)
        if end - m2 > m1 - start:
            quick_sort(arr, start, m1)
            start = m2 + 1
        else:
            quick_sort(arr, m2 + 1, end)
            end = m1




if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    quick_sort(arr, 0, n)
    print(' '.join([str(x) for x in arr]))
