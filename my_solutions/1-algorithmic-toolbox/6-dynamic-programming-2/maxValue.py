arr = list(input())
number_of_operations = len(arr) // 2
num_of_numbers = number_of_operations + 1

import numpy as np
m = np.zeros((num_of_numbers, num_of_numbers))
M = np.zeros((num_of_numbers, num_of_numbers))
import operator
opt = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.sub}

def min_and_max(i:int, j:int):
    mini = float('inf')
    maxi = float('-inf')
    for k in range(i, j):
        a = opt[arr[k * 2 + 1]](M[i, k], M[k + 1, j])
        b = opt[arr[k * 2 + 1]](m[i, k], M[k + 1, j])
        c = opt[arr[k * 2 + 1]](M[i, k], m[k + 1, j])
        d = opt[arr[k * 2 + 1]](m[i, k], m[k + 1, j])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a , b, c, d)
    return mini, maxi


for i in range(num_of_numbers):
    m[i,i], M[i,i] = arr[i * 2], arr[i * 2]

for s in range(1, num_of_numbers):
    for i in range(num_of_numbers - s):
        j = i + s
        m[i,j], M[i,j] = min_and_max(i, j)

print(int(M[0 , num_of_numbers - 1]))
