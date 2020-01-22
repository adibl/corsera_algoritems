len1 = input()
str1 = input().split()
len2 = input()
str2 = input().split()
len3 = input()
str3 = input().split()
import numpy as np

arr = np.zeros((len(str1) + 1, len(str2) + 1, len(str3) + 1), dtype=int)

for i in range(1, len(str1) + 1):
    for j in range(1,len(str2) + 1):
        for g in range(1, len(str3) + 1):
            options = []
            options.append(arr[i][j - 1][g])
            options.append(arr[i - 1][j][g])
            if str1[i - 1] == str2[j - 1] == str3[g - 1]:
                options.append(arr[i - 1][j - 1][g - 1] + 1)
            else:
                options.append(arr[i - 1][j - 1][g - 1])
            options.sort()
            arr[i][j][g] = options[-1]
print(arr[-1][-1][-1])
