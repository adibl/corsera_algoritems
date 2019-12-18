n, W = [int(x) for x in input().split()]
arr = []
for i in range(0, n):
    value, w = [int(x) for x in input().split()]
    arr.append([w, value / w])


arr = sorted(arr, key=lambda x: x[1])

total_value = 0
while W > 0:
    w, value_per_1 = arr.pop()
    w_take = min(w, W)
    total_value += w_take * value_per_1
    W -= w_take
print("{0:.4f}".format(total_value))


