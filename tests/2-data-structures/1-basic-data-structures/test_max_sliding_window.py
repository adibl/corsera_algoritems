import pytest
import random
import string
import sys
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/1-basic-data-structures/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/1-basic-data-structures/'
    FILE_NAME = 'max_sliding_window.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 5

    @classmethod
    def number(cls): return random.randrange(1,10 ** 4)

    @classmethod
    def number2(cls): return random.randrange(0, 10 ** 4)

    def data_creator(self):
        len1 = self.number()
        window_len = random.randrange(1, len1 + 1)
        s = str(len1) + '\n'
        s += str(self.number2())
        for i in range(len1 - 1):
            s += ' ' + str(self.number2())
        s += '\n'
        s += str(window_len) + '\n'
        return s

if __name__ == '__main__':
    test = Test_spec()
    test.main()

def test_my_only():
    test = Test_spec()
    assert test.unit_test('8\n2 7 3 1 5 2 6 2\n4') == '7 7 5 6 6'
    assert test.unit_test('8\n2 7 3 1 5 2 6 2\n2') == '7 7 3 5 5 6 6'
 # bag, dont see thet the proc didint finish yet


