import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    FILE_NAME = 'nInversions.py'
    PERMOTATIONS = 100

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 5)

    @classmethod
    def number2(cls): return random.randrange(1, 10 ** 9)

    def data_creator(self):
        n = self.number()
        s = str(n) + '\r\n'
        s += str(self.number2())
        for i in range(1, n):
            s += ' ' + str(self.number2())
        s += '\r\n'
        return s


if __name__ == '__main__':
    Test_spec().main()
