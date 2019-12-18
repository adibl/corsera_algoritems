from functools import cmp_to_key
n = int(input())
arr = input().split()


def cmp(num1, num2):
    numbers = [str(num1), str(num2)]
    return int(numbers[1] + numbers[0]) - int(numbers[0] + numbers[1])


arr.sort(key=cmp_to_key(cmp))
print(''.join(arr))

