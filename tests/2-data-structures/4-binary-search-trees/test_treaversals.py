import string
import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/4-binary-search-trees/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/4-binary-search-trees/'
    IS_PRINT_OUTPUTS = True
    SEE_STDERR = True
    FILE_NAME = 'traversals.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 6

    @classmethod
    def node_number(cls):
        return random.randint(10, 100)

    @classmethod
    def node_value(cls):
        return random.randint(1, 100)

    def data_creator(self):
        tree_size = self.node_number()
        arr = [[None, None, None] for _ in range(tree_size)]

        next_empty = 0
        arr[0] = [self.node_value(), None, None]
        next_empty = 1
        while next_empty < len(arr):
            value = self.node_value()
            index = 0
            while arr[index] is not None:
                if value < arr[index][0]:
                    if arr[index][1] is not None:
                        index = arr[index][1]
                    else:
                        arr[index][1] = next_empty
                        arr[next_empty][0] = value
                        next_empty += 1
                        break
                elif value > arr[index][0]:
                    if arr[index][2] is not None:
                        index = arr[index][2]
                    else:
                        arr[index][2] = next_empty
                        arr[next_empty][0] = value
                        next_empty += 1
                        break
                else:
                    break
        s = str(tree_size) + '\n'
        for var in arr:
            var = [-1 if x is None else x for x in var]
            s += ' '.join([str(x) for x in var]) + '\n'
        print(s)
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()
