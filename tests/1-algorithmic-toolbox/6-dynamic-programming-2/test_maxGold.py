import random
import string
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/6-dynamic-programming-2/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/6-dynamic-programming-2/'
    FILE_NAME = 'maxGold.py'
    PERMOTATIONS = 100

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 3)

    @classmethod
    def number2(cls): return random.randrange(0, 10 ** 5)

    @classmethod
    def number3(cls): return random.randrange(1, 300)

    def data_creator(self):
        len1 = self.number3()
        max_size = self.number()
        s = str(max_size) + ' ' + str(len1)
        s += '\n'
        s += str(self.number3())
        for i in range(1, len1):
            s+= ' ' + str(self.number3())
        return s

if __name__ == '__main__':
    Test_spec().main()
