import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/2-priority-queues-and-disjoint-sets/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/2-priority-queues-and-disjoint-sets/'
    FILE_NAME = 'merging_tables.py'
    PERMOTATIONS = 100
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    TIME_LIMIT = 6.0

    @classmethod
    def number(cls): return random.randrange(1, 100000)

    @classmethod
    def number2(cls): return random.randrange(0, 10000)

    def data_creator(self):
        num_of_tables = self.number()
        num_of_union = self.number()
        s = str(num_of_tables) + ' ' + str(num_of_union) + '\n'
        for _ in range(num_of_tables):
            s += str(self.number2()) + ' '
        s = s[:-1] + '\n'
        for _ in range(num_of_union):
            s += str(random.randrange(1, num_of_tables + 1)) + ' ' + \
                str(random.randrange(1, num_of_tables + 1)) + '\n'
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()


def test_my():
    test = Test_spec()
    assert test.unit_test('5 5\n1 1 1 1 1\n3 5\n2 4\n1 4\n5 4\n5 3\n') == '2\n2\n3\n5\n5'
