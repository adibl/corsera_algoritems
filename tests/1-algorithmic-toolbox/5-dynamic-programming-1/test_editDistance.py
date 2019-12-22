import random
import string
import test_class 


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/5-dynamic-programming-1/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/5-dynamic-programming-1/'
    FILE_NAME = 'editDistance.py'
    PERMOTATIONS = 500

    @classmethod
    def number(cls): return random.randrange(1, 100)

    def data_creator(self):
        len1 = self.number()
        len2 = self.number()
        options = [char for char in string.ascii_lowercase]
        str1 = "".join([random.choice(options) for x in range(0, len1)])
        str2 = "".join([random.choice(options) for x in range(0, len2)])
        return str1 + '\n' + str2

if __name__ == '__main__':
    Test_spec().main()
