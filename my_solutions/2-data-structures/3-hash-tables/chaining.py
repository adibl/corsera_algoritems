from hashtable import HashTable


def PolyHashFunction(p, x, m):
    return lambda string: sum([ord(string[i]) * (x ** i) for i in range(len(string))]) % p % m


if __name__ == "__main__":
    m = int(input())
    HashTable.M = m
    h = HashTable(hash_function=PolyHashFunction(1000000007, 263, m))
    number_of_lines = int(input())
    to_print = []
    for _ in range(number_of_lines):
        line = input().split()
        if line[0] == 'find':
            to_print.append(h.is_value(line[1]))
        elif line[0] == 'del':
            h.remove(line[1])
        elif line[0] == 'add':
            h.add(line[1])
        elif line[0] == 'check':
            node = h.arr[int(line[1])]
            s = ''
            while node is not None:
                s += node.get_value() + ' '
                node = node.pointer
            to_print.append(s[:-1])
    for var in to_print:
        if var is None:
            print('')
        elif var is True:
            print('yes')
        elif var is False:
            print('no')
        else:
            print(var)
