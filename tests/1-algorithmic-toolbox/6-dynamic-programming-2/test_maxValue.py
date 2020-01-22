import random
import string
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/6-dynamic-programming-2/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/6-dynamic-programming-2/'
    FILE_NAME = 'maxValue.py'
    PERMOTATIONS = 100

    @classmethod
    def number(cls): return random.randrange(1, 14)

    @classmethod
    def number2(cls): return random.randrange(0, 9)

    def data_creator(self):
        operators = ['-', '+', '*']
        len1 = self.number()
        s = ''
        s += str(self.number2())
        for i in range(1, len1):
            s += random.choice(operators)
            s += str(self.number2())
        return s

if __name__ == '__main__':
    Test_spec().main()
