# python 3
str1 = input()
str2 = input()
arr = [[], ]
import pdb;pdb.set_trace()
for i in range(0, len(str2) + 1):
    arr[0].append(i)

for i in range(1, len(str1) + 1):
    arr.append([i])

for i in range(1, len(str1) + 1):
    for j in range(1,len(str2) + 1):
        options = []
        options.append(arr[i][j - 1] + 1)
        options.append(arr[i - 1][j] + 1)
        if str1[i - 1] == str2[j - 1]:
            options.append(arr[i - 1][j - 1])
        else:
            options.append(arr[i - 1][j - 1] + 1)
        options.sort()
        arr[i].append(options[0])
# ioxof, og error
print(arr[-1][-1])
