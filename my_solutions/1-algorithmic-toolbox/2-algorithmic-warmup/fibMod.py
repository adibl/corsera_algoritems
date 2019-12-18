# python 3
n, m = [int(x) for x in input().split()]
fibo = [0, 1]
pisado = [0, 1]
fibo.append(fibo[-1] + fibo[-2])
pisado.append(fibo[-1] % m)
while pisado[-2:] != [0, 1]:
    fibo.append(fibo[-1] + fibo[-2])
    pisado.append(fibo[-1] % m)
pisado_len = len(pisado) - 2
small_n = n % pisado_len

while small_n > len(fibo):
    fibo.append(fibo[-1] + fibo[-2])
print(fibo[small_n] % m)
