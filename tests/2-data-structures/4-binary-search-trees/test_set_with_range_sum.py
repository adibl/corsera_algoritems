import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/4-binary-search-trees/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/4-binary-search-trees/'
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    FILE_NAME = 'set_with_range_sum.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 20

    @classmethod
    def line_num(cls):
        return random.randint(1, 100000)

    @classmethod
    def number(cls):
        return random.randint(1, 10 ** 9)

    def data_creator(self):
        num_of_lines = self.line_num()
        s = str(num_of_lines) + '\n'
        options = ['+', '-', '?', 's']
        for _ in range(num_of_lines):
            opt = random.choice(options)
            if opt == '+':
                s += '+ ' + str(self.number()) + '\n'
            elif opt == '-':
                s += '- ' + str(self.number()) + '\n'
            elif opt == '?':
                s += '? ' + str(self.number()) + '\n'
            elif opt == 's':
                numbers = [self.number(), self.number()]
                numbers.sort()
                s += 's ' + str(numbers[0]) + ' ' + str(numbers[1]) + '\n'
        return s

if __name__ == '__main__':
    test = Test_spec()
    test.test_aginst_function()


def test_minimul():
    test = Test_spec()
    assert test.unit_test(
        "5\n? 0\n+ 0\n? 0\n- 0\n? 0\n") == "Not found\nFound\nNot found"


def test_sum_range():
    test = Test_spec()
    assert test.unit_test(
        "5\n+ 491572259\n? 491572259\n? 899375874\ns 310971296 877523306\n+ 352411209\n"
    ) == "Found\nNot found\n491572259"


def test_mod_m():
    test = Test_spec()
    assert test.unit_test(
        "15\n? 1\n+ 1\n? 1\n+ 2\ns 1 2\n+ 1000000000\n? 1000000000\n- 1000000000\n? 1000000000\ns 999999999 1000000000\n- 2\n? 2\n- 0\n+ 9\ns 0 9\n"
    ) == "Not found\nFound\n3\nFound\nNot found\n1\nNot found\n10"
