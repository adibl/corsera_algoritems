import random
import string
import test_class 


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/5-dynamic-programming-1/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/5-dynamic-programming-1/'
    FILE_NAME = 'lcs2.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 100)

    @classmethod
    def number2(cls): return random.randrange(-10 ** 9 , 10 ** 9)

    def data_creator(self):
        len1 = self.number()
        len2 = self.number()
        str1 = " ".join(str(self.number2()) for x in range(len1))
        str2 = " ".join(str(self.number2()) for x in range(len2))
        s = str(len1) + '\n'
        s += str1 + '\n'
        s += str(len2) + '\n'
        s += str2 + '\n'
        return s


if __name__ == '__main__':
    Test_spec().main()
