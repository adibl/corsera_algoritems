len1 = input()
str1 = input().split()
len2 = input()
str2 = input().split()
# python 3 editDistance.py
arr = [[], ]
for i in range(0, len(str2) + 1):
    arr[0].append(0)

for i in range(1, len(str1) + 1):
    arr.append([0])

for i in range(1, len(str1) + 1):
    for j in range(1,len(str2) + 1):
        options = []
        options.append(arr[i][j - 1])
        options.append(arr[i - 1][j])
        if str1[i - 1] == str2[j - 1]:
            options.append(arr[i - 1][j - 1] + 1)
        else:
            options.append(arr[i - 1][j - 1])
        options.sort()
        arr[i].append(options[-1])
print(arr[-1][-1])
