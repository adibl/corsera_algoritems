import random
import re
from test_class import Test

class Test_spec(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/5-dynamic-programming-1/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/5-dynamic-programming-1/'
    FILE_NAME = 'primitiveCalc.py'
    PERMOTATIONS = 1000

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 5)

    def data_creator(self):
        return str(self.number())

    def compare_output(self, my_result, course_result):
        my_number, numbers, *_ = re.split(r'\\n', my_result)
        course_number, *_ = re.split(r'\\n', course_result)
        numbers = [int(x) for x in numbers.split(' ')]
        for i in range(1, len(numbers)):
            prev = numbers[i - 1]
            current = numbers[i]
            if prev + 1 == current or prev * 3 == current or prev * 2 == current:
                pass
            else:
                return False
        return my_number == course_number


if __name__ == '__main__':
    Test_spec().main()
