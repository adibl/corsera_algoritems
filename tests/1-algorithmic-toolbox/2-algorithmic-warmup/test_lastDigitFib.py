import random
from tests import Test


class TestLastDigit(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    FILE_NAME = 'lastDigitFib.py'
    PERMOTATIONS = 100


    @classmethod
    def number(cls): return random.randrange(10 ** 6, 10 ** 7)

    def data_creator(self):
        return str(self.number())


if __name__ == '__main__':
    TestLastDigit().main()
