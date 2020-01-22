import random
import string
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/1-basic-data-structures/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/1-basic-data-structures/'
    FILE_NAME = 'brackets.py'
    PERMOTATIONS = 100

    @classmethod
    def number(cls): return random.randrange(1,10 ** 5)

    @classmethod
    def char(cls):
        if random.randint(1, 6) == 6:
            return random.choice(string.ascii_letters + string.digits)
        else:
            return random.choice(['[', ']', '{', '}', '(', ')'])

    def data_creator(self):
        len1 = self.number()
        s = ''
        s += str(self.char())
        for i in range(1, len1):
            s += self.char()
        return s

if __name__ == '__main__':
    Test_spec().main()
