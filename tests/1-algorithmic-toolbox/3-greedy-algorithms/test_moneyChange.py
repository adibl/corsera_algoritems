import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    FILE_NAME = 'moneyChange.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 3)

    def data_creator(self):
        return str(self.number())


if __name__ == '__main__':
    Test_spec().main()