# python 3

sum_last_fibonaci = [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6,
                     4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]
n = int(input())
# total = n // len(sum_last_fibonaci) * 280 # sum(sequence) last digit 0
print(sum_last_fibonaci[n % 60])  # len(sum_last_fibo
