import random
from tests import Test


class TestAlgo(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    FILE_NAME = 'maxPrizes.py'
    PERMOTATIONS = 1000

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 9)

    def data_creator(self):
        return str(self.number())


if __name__ == '__main__':
    TestAlgo().main()
