def signitures(arr):
    if len(arr) < 2:
        return [x[2] for x in arr]
    line = arr.pop()
    line2 = arr.pop()
    start_change = line[0] - line2[0]
    if (start_change < 0 and line[1] >= -1 * start_change) or (start_change > 0 and line2[1] >= start_change) or start_change == 0:
            start = max(line[0], line2[0])
            end = min(line[2], line2[2])
            arr.append([start, end - start, end])
            x = signitures(arr)
            return x

    else:
        arr.append(line2)
        x = signitures(arr)
        x.append(line[2])
        return x


n = int(input())
arr = []
for i in range(0, n):
    start, end = [int(x) for x in input().split()]
    arr.append([start, end - start, end])
arr.sort(key=lambda x: x[0], reverse=True)
arr = signitures(arr)
print(len(arr))
s = ''
for num in reversed(arr):
    s += str(num) + ' '
s = s[:-1]
s += '\r\n'
print(s)

