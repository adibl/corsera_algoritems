import string
import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/3-hash-tables/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/3-hash-tables/'
    FILE_NAME = 'hash_substring.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 10.0

    @classmethod
    def string_length(cls): return random.randrange(1, 5 * 10 ** 5)

    @classmethod
    def create_string(cls, length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def data_creator(self):
        string = self.create_string(self.string_length())
        pattern = self.create_string(random.randint(1, len(string)))
        return pattern + '\n' + string + '\n'


if __name__ == '__main__':
    test = Test_spec()
    test.main()
