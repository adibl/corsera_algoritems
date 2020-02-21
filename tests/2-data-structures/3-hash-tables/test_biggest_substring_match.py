import string
import random
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/3-hash-tables/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/3-hash-tables/'
    # IS_PRINT_OUTPUTS = True
    SEE_STDERR = True
    FILE_NAME = 'biggest_substring_match.py'
    PERMOTATIONS = 100
    TIME_LIMIT = 15.0
    LENGTH_REMAIN = 100000

    def __init__(self):
        super().__init__()
        self.length_remain1 = self.LENGTH_REMAIN
        self.length_remain2 =self.LENGTH_REMAIN

    def num_of_subequal(self, length_remain_number):
        if length_remain_number == 1:
            if self.length_remain1 <= 1:
                return 1
            ret = random.randrange(1, self.length_remain1)
            self.length_remain1 -= ret 
        elif length_remain_number == 2:
            if self.length_remain2 <= 1:
                return 1
            ret = random.randrange(1, self.length_remain2)
            self.length_remain2 -= ret
        else:
            raise NotImplemented
        return ret

    @classmethod
    def create_string(cls, length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def data_creator(self):
        self.length_remain1 = self.LENGTH_REMAIN
        self.length_remain2 =self.LENGTH_REMAIN
        s = ''
        for _ in range(3):
            string1 = self.create_string(self.num_of_subequal(1))
            string2 = self.create_string(self.num_of_subequal(2))
            s += string1 + ' ' + string2 + '\n'
        return s

    def validate_result(self, result, data):
        data_lines = data.split('\n')[:-1] 
        result_lines = result.split('\n')[:-1]
        for data_line, result_line in zip(data_lines, result_lines):
            string1, string2 = data_line.split(' ')
            index1, index2, length = [int(x) for x in result_line.split(' ')]
            if string1[index1: index1 + length] == string2[index2: index2 + length]:
                return True
            return False


if __name__ == '__main__':
    test = Test_spec()
    test.test_aginst_function()
