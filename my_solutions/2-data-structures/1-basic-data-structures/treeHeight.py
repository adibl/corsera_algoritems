def get_hight(dictionary):
    root = dictionary['-1']
    next_indexes = []
    indexes = root
    #import pdb;pdb.set_trace()
    deapth = 0
    while len(indexes) > 0:
        for ind in indexes:
            if ind in dictionary:
                next_indexes.extend(dictionary[ind])
        deapth += 1
        indexes = next_indexes
        next_indexes = []
    return deapth


def main(test_param=None):
    n = input()
    arr = input().split()
    dictionary = {}
    num = 0
    for var in arr:
        if var in dictionary:
            dictionary[var].append(str(num))
        else:
            dictionary[var] = [str(num)]
        num += 1
    print(get_hight(dictionary))

if __name__ == "__main__":
    main()

