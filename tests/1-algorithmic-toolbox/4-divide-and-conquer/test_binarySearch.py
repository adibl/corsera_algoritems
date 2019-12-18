import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    FILE_NAME = 'binarySearch.py'
    PERMOTATIONS = 1000

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 4)

    @classmethod
    def number2(cls): return random.randrange(1, 10 ** 9)

    def data_creator(self):
        n = self.number()
        s = str(n)
        for i in range(0, n):
            s += ' ' + str(self.number2())
        s += '\r\n'
        n = self.number()
        s += str(n)
        for i in range(0, n):
            s += ' ' + str(self.number2())
        s += '\r\n'
        return s

if __name__ == '__main__':
    Test_spec().main()