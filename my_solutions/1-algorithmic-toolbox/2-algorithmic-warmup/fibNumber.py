if __name__ == '__main__':
    n = input()
    if n == 0:
        print(0)
        exit()
    if n == 1:
        print(1)
        exit()
    x1 = 0
    x2 = 1
    x3 = 0
    for i in range(int(n) - 1):
        x3 = x1 + x2
        print(x3)
        x1 = x2
        x2 = x3
    print(str(x3))

