import random
from tests import Test


class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/4-divide-and-conquer/'
    FILE_NAME = 'Lottery.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 50000)


    @classmethod
    def number2(cls): return random.randrange(-10 ** 8, 10 ** 8)

    def data_creator(self):
        s, p = self.number(), self.number()
        ret = str(s) + ' ' + str(p) + '\r\n'
        for i in range(0, s):
            num1, num2 = self.number2(), self.number2()
            ret += str(min(num1, num2)) + ' ' + str(max(num1, num2))
        ret += str(self.number2())
        for i in range(1, p):
            ret += ' ' + str(self.number2())
        return ret

if __name__ == '__main__':
    Test_spec().main()