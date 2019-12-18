import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    FILE_NAME = 'maxRevenue.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(-10 ** 5, 10 ** 5)

    @classmethod
    def number2(cls): return random.randrange(1, 10 ** 3)

    def data_creator(self):
        n = self.number2()
        s = str(n) + '\r\n'
        s += str(self.number())
        for i in range(1, n):
            s += " " + str(self.number())
        s += "\r\n"
        s += str(self.number())
        for i in range(1, n):
            s += " " + str(self.number())
        s += "\r\n"
        return s


if __name__ == '__main__':
    Test_spec().main()