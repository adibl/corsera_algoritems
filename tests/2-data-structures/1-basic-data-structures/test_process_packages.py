import pytest
import random
import string
import sys
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/1-basic-data-structures/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/1-basic-data-structures/'
    FILE_NAME = 'process_packages.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 10

    @classmethod
    def number(cls): return random.randrange(1,10 ** 5)

    @classmethod
    def number2(cls): return random.randrange(0,10 ** 5)

    @classmethod
    def number3(cls): return random.randrange(0,10 ** 3)

    @classmethod
    def number4(cls): return random.randrange(0,10 ** 6)


    def data_creator(self):
        len1 = self.number2()
        stack_size = self.number()
        s = str(stack_size) + ' ' + str(len1)
        arr = []
        for num in range(len1):
            arr.append((self.number4(), self.number3()))
        arr.sort(key= lambda x: x[0])
        for var in arr:
            s += str(var[0]) + ' ' + str(var[1])
            s += '\n'
        return s

if __name__ == '__main__':
    test = Test_spec()
    test.main()

def test_my_only():
    test = Test_spec()
    assert test.unit_test('1 2\n0 1\n0 1\n') == "b'0\\n-1\\n'"
    assert test.unit_test('1 2\n0 1\n1 1\n') == "b'0\\n1\\n'"
    assert test.unit_test('1 0\n') == "b''"
 # bag, dont see thet the proc didint finish yet


