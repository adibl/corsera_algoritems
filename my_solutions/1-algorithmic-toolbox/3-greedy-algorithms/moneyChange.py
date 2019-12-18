# python 3
n = int(input())
sum = n // 10
n = n % 10
sum += n // 5
sum += n % 5
print(sum)
