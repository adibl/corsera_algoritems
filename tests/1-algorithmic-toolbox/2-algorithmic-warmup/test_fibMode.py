import random
from tests import Test


class TestfibMode(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    FILE_NAME = 'fibMod.py'
    PERMOTATIONS = 1000

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 18)

    @classmethod
    def number2(cls): return random.randrange(2, 10 ** 3)

    def data_creator(self):
        return str(self.number()) + " " + str(self.number2())


if __name__ == '__main__':
    TestfibMode().main()
