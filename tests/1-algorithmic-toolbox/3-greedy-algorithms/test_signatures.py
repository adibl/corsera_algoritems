import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    FILE_NAME = 'signatures.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 100)

    @classmethod
    def number2(cls): return random.randrange(1, 10 ** 9)

    def data_creator(self):
        n = self.number()
        s = str(n) + '\r\n'
        for i in range(0, n):
            nums = [self.number2(), self.number2()]
            s += str(min(nums)) + ' ' + str(max(nums)) + '\r\n'
        return s



if __name__ == '__main__':
    Test_spec().main()