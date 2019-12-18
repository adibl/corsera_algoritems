def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


num1, num2 = input().split()
print(gcd(num2, num1))
