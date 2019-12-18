import random
from tests import Test

class Test_algo(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/1-programming-challenges/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/1-programming-challenges/'
    FILE_NAME = 'maxPairwiseProduct.py'
    MB_LIMIT = 5012
    TIME_LIMIT = 5.0
    @classmethod
    def number(cls): return random.randrange(2, 2 * 10 ** 5)
    PERMOTATIONS = 100

    def data_creator(self):
        numbers = ''
        for x in range(self.number() - 1):
            numbers += " " + str(self.number())
        return str(len(numbers)) + '\n' + numbers

if __name__ == '__main__':
    Test_algo().main()


