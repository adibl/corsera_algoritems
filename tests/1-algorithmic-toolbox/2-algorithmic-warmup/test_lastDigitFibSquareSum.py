import random
from tests import Test


class TestLastDigit(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    FILE_NAME = 'lastDigitFibSquareSum.py'
    PERMOTATIONS = 10000

    @classmethod
    def number(cls): return random.randrange(0, 10 ** 18)

    def data_creator(self):
        return str(self.number())


if __name__ == '__main__':
    TestLastDigit().main()
