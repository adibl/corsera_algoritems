import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/2-priority-queues-and-disjoint-sets/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/2-priority-queues-and-disjoint-sets/'
    FILE_NAME = 'parallelProcessing.py'
    PERMOTATIONS = 100
    #SEE_STDERR = True
    TIME_LIMIT = 10.0

    @classmethod
    def number(cls): return random.randrange(10 ** 4, 10 ** 5)

    @classmethod
    def number2(cls): return random.randrange(0, 10 ** 9)

    def data_creator(self):
        thread_number = self.number()
        arr_len = self.number()
        s = str(thread_number) + ' ' + str(arr_len) + '\n'
        for _ in range(arr_len):
            s += str(self.number2()) + ' '
        s = s[:-1] + '\n'
        return s


if __name__ == '__main__':
    test = Test_spec()
    test.main()
