import string
import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/3-hash-tables/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/3-hash-tables/'
    FILE_NAME = 'chaining.py'
    PERMOTATIONS = 100
    SOME_NAME = 7.0

    @classmethod
    def number(cls): return random.randrange(10, 10 ** 5)

    @classmethod
    def name_length(cls): return random.randrange(1, 15)

    @classmethod
    def name(cls):
        length = cls.name_length()
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def data_creator(self):
        names = []

        num_of_lines = self.number()
        array_length = random.randint(num_of_lines // 5, num_of_lines)
        s = str(array_length) + '\n' + str(num_of_lines) + '\n'
        for _ in range(num_of_lines):
            action = random.choice(['add', 'del', 'find'])
            if action == 'add':
                name = self.name()
                names.append(name)
                s += 'add ' + self.name() + '\n'
            elif action == 'del':
                if random.randint(0, 6) != 0 and len(names) > 0:
                    name = random.choice(names)
                    names.remove(name)
                else:
                    name = self.name()
                s += 'del ' + str(name) + '\n'
            elif action == 'find':
                if random.randint(0, 6) != 0 and len(names) > 0:
                    name = random.choice(names)
                    names.remove(name)
                else:
                    name = self.name()
                s += 'find ' + str(name) + '\n'
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()


def test_my():
    test = Test_spec()
    assert test.unit_test("5\n3\nadd world\nadd HellO\ncheck 4\n") == "HellO world"
    assert test.unit_test(
        "7\n9\nadd LlfcqqOBhGog\nfind ycA\nadd gBfPCgrqkS\nadd KhjIG\ndel ayvcJyKEXsDYf\nadd v\nadd fPGCu\nfind TTcXTozspxzHo\ndel B\n") == "HellO world"


def test_from_pdf():
    test = Test_spec()
    test.unit_test("5\n12\nadd world\nadd HellO\ncheck 4\nfind World\nfind world\ndel world\ncheck 4\ndel HellO\nadd luck\nadd GooD\ncheck 2\ndel good") == 'HellO world\nno\nyes\nHellO\nGooD luck'
    test.unit_test(
        "4\n8\nadd test\nadd test\nfind test\ndel test\nfind test\nfind Test\nadd Test\nfind Test") == "yes\nno\nno\nyes"
    test.unit_test("3\n12\ncheck 0\nfind help\nadd help\nadd del\nadd add\nfind add\nfind del\ndel del\nfind del\ncheck 0\ncheck 1\ncheck 2") == "\nno\nyes\nyes\nno\n\nadd help"
