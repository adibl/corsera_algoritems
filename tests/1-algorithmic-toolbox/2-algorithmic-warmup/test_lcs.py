import random
from tests import Test


class TestLca(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/2-algorithmic-warmup/'
    FILE_NAME = 'lcm.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 2 * 10 ** 9)

    def data_creator(self):
        return str(str(self.number()) + " " + str(self.number()))


if __name__ == '__main__':
    TestLca().main()
