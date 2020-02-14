import numpy

if __name__ == "__main__":
    arr = numpy.empty((10 ** 7), dtype='S15')
    to_print = []
    n = int(input())
    for _ in range(n):
        line = input().split()
        if line[0] == 'add':
            arr[int(line[1])] = line[2].encode('ascii')
        elif line[0] == 'del':
            arr[int(line[1])] = ''
        elif line[0] == 'find':
            to_print.append(arr[int(line[1])])
    for var in to_print:
        if var.decode('ascii') == '':
            print('not found')
        else:
            print(var.decode('ascii'))
