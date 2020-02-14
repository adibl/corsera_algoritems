import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/2-priority-queues-and-disjoint-sets/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/2-priority-queues-and-disjoint-sets/'
    FILE_NAME = 'arrayToHeap.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 3.0

    @classmethod
    def number(cls): return random.randrange(1, 100000)

    @classmethod
    def number2(cls): return random.randrange(0, 10 ** 9)

    def data_creator(self):
        arr_len = self.number()
        numbers = set()
        s = str(arr_len) + '\n'
        while len(numbers) != arr_len:
            numbers.add(self.number2())
        for num in numbers:
            s += str(num) + ' '
        s = s[:-1] + '\n'
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()


def test_my_only():
    test = Test_spec()
    assert test.unit_test('5\n5 4 3 2 1') == '3\n1 4\n0 1\n1 3'
    assert test.unit_test('5\n1 2 3 4 5') == '0'
