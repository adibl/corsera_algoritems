n = int(input())
arr = [1]
count = 1
num = arr[-1] + 1
while num <= n:
    arr.append(num)
    n -= num
    count += 1
    num = arr[-1] + 1
arr[-1] += n - n
print(count)
print(' '.join([str(x) for x in arr]))