import pytest
import random
import string
import sys
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/1-basic-data-structures/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/1-basic-data-structures/'
    FILE_NAME = 'stack_with_max_naive.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 5
    __OPTIONS = ['push', 'pop', 'max']

    @classmethod
    def number(cls): return random.randrange(1,400000)

    @classmethod
    def number2(cls): return random.randrange(0, 10 ** 5)

    def data_creator(self):
        import pdb;pdb.set_trace()
        len1 = self.number()
        s = str(len1) + '\n'
        for i in range(len1):
            option = random.choice(self.__OPTIONS)
            if option == self.__OPTIONS[0]:
                option += ' ' + str(self.number2())
            s += option + '\n'
        return s

if __name__ == '__main__':
    test = Test_spec()
    test.main()

def test_my_only():
    test = Test_spec()
    assert test.unit_test('5\npush 2\npush 1\n max\npop\nmax') == "b'2\\n2\\n'"
    assert test.unit_test('5\npush 1\npush 2\n max\npop\nmax') == "b'2\\n1\\n'"
    assert test.unit_test('10\npush 2\npush 3\npush 9\npush 7\npush 2\n max\nmax\nmax\npop\nmax\n') == "b'9\\n9\\n9\\n9\\n'"
    assert test.unit_test('3\npush1\npush7\npop\n') == "b''"
 # bag, dont see thet the proc didint finish yet


