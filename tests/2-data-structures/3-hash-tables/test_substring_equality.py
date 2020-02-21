import string
import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/3-hash-tables/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/3-hash-tables/'
    # IS_PRINT_OUTPUTS = True
    # SEE_STDERR = True
    FILE_NAME = 'substring_equality.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 10.0

    @classmethod
    def string_length(cls): return random.randrange(1, 500000)

    @classmethod
    def num_of_subequal(cls): return random.randrange(1, 100000)

    @classmethod
    def create_string(cls, length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def data_creator(self):
        text = self.create_string(self.string_length())
        s = text + '\n'
        num_of_lines = self.num_of_subequal()
        s += str(num_of_lines) + '\n'
        def index(): return random.randrange(0, len(text))
        for _ in range(num_of_lines):
            indexes = [index(), index()]
            indexes.sort()
            length = random.randrange(0, len(text) - indexes[-1])
            s += str(indexes[0]) + ' ' + str(indexes[1]) + ' ' + str(length) + '\n'
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()
