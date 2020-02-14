import string
import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/3-hash-tables/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/3-hash-tables/'
    FILE_NAME = 'phoneBook.py'
    PERMOTATIONS = 100
    MAX_VIRTUAL_MEMORY = 512 * 1024 * 1024
    TIME_LIMIT = 6.0

    @classmethod
    def number(cls): return random.randrange(1, 10 ** 5)

    @classmethod
    def name_length(cls): return random.randrange(1, 15)

    @classmethod
    def name(cls):
        length = cls.name_length()
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    @classmethod
    def phone_number(cls): return random.randrange(1, 9999999)

    def data_creator(self):
        numbers = []
        num_of_lines = self.number()
        s = str(num_of_lines) + '\n'
        for _ in range(num_of_lines):
            action = random.choice(['add', 'del', 'find'])
            if action == 'add':
                number = self.phone_number()
                numbers.append(number)
                s += 'add ' + str(number) + ' ' + self.name() + '\n'
            elif action == 'del':
                if random.randint(0, 6) != 0 and len(numbers) > 0:
                    number = random.choice(numbers)
                    numbers.remove(number)
                else:
                    number = self.phone_number()
                s += 'del ' + str(number) + '\n'
            elif action == 'find':
                if random.randint(0, 6) != 0 and len(numbers) > 0:
                    number = random.choice(numbers)
                    numbers.remove(number)
                else:
                    number = self.phone_number()
                s += 'find ' + str(number) + '\n'
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()


def test_my():
    test = Test_spec()
    assert test.unit_test('1\nfind 345\n') == 'not found'


def test_from_pdf():
    test = Test_spec()
    assert test.unit_test(
        "12\nadd 911 police\nadd 76213 Mom\nadd 17239 Bob\nfind 76213\nfind 910\nfind 911\ndel 910\ndel 911\nfind 911\nfind 76213\nadd 76213 daddy\nfind 76213\n") == "Mom\nnot found\npolice\nnot found\nMom\ndaddy"
