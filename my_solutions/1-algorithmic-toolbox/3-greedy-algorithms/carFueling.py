d = int(input())
m = int(input())
n = int(input())
arr = [int(x) for x in input().split()]
stop_number = 0
current_place = 0
for num in range(1, n):
    if current_place + m >= d:
        break
    elif arr[num] > current_place + m:
        current_place = arr[num-1]
        stop_number += 1
    elif num == n - 1:
        current_place = arr[num]
        stop_number += 1
if current_place + m >= d:
    print(stop_number)
else:
    print("-1")

