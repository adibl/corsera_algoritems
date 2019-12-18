import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    FILE_NAME = 'closestsPoints.py'
    PERMOTATIONS = 100

    @classmethod
    def number(cls): return random.randrange(2, 10 ** 4)

    @classmethod
    def number2(cls): return random.randrange(-10 ** 9, 10 ** 9)

    def data_creator(self):
        n = self.number()
        s = str(n) + '\r\n'
        for i in range(0, n):
            s += '{0} {1}\r\n'.format(self.number2(), self.number2())
        return s

if __name__ == '__main__':
    Test_spec().main()