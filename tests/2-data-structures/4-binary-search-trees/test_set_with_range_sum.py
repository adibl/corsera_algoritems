import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/4-binary-search-trees/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/4-binary-search-trees/'
    #IS_PRINT_OUTPUTS = True
    SEE_STDERR = True
    FILE_NAME = 'set_with_range_sum.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 120
    @classmethod
    def line_num(cls):
        return random.randint(1, 100000)

    @classmethod
    def number(cls):
        return random.randint(1, 10 ** 9)

    def data_creator(self):
        num_of_lines = self.line_num()
        print(num_of_lines)
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

    def validate_result(self, result, data):
        arr = set()
        data = data.split('\n')
        result = result.split('\n')
        i = 0
        m = 1000000001
        x = 0
        for line in data[1:]:
            line = line.split(' ')
            operator = line[0]
            numbers = [(int(num) + x) % m for num in line[1:]]
            if operator == '+':
                arr.add(numbers[0])
            elif operator == '-':
                arr.discard(numbers[0])
            elif operator == '?':
                is_found = numbers[0] in arr
                if is_found:
                    if result[i] != "Found":
                        print('number {0} is in the set'.format(numbers[0]))
                        return False
                else:
                    if result[i] != "Not found":
                        print('number {0} is not in the set'.format(numbers[0]))
                        return False
                i += 1
            elif operator == 's':
                bottom, top = numbers[0], numbers[1]
                res = 0
                for var in arr:
                    if bottom <= var <= top:
                        res += var
                x = res
                if str(res) != result[i]:
                    print('sum is {0} and should be {1}'.format(result[i], res))
                    return False
                i += 1
        return True


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
