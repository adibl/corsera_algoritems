import random
from tests import Test


class TestAlgo(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    FILE_NAME = 'maxLoot.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 3)

    @classmethod
    def number2(cls): return random.randrange(0, 2 * 10 ** 6)

    def data_creator(self):
        n = self.number()
        s = str(n) + " " + str(self.number2())+ "\r\n"
        for i in range(0, n):
            s+= str(self.number2()) + " " + str(self.number2()) + '\r\n'
        return s


if __name__ == '__main__':
    TestAlgo().main()
