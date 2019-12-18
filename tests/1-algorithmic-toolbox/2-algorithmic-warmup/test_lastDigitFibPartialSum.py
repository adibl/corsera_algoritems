import random
from tests import Test


class TestLastFibPartialSum(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    FILE_NAME = 'lastDigitFibPartialSum.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(0, 10 ** 18 - 1)

    @classmethod
    def number2(cls, num): return random.randrange(num, 10 ** 18)

    def data_creator(self):
        num = self.number()
        return str(num) + " " + str(self.number2(num))


if __name__ == '__main__':
    TestLastFibPartialSum().main()
