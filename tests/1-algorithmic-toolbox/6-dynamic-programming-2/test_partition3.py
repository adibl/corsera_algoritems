import random
import sys
import string
import test_class



class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/6-dynamic-programming-2/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/6-dynamic-programming-2/'
    FILE_NAME = 'partition3.py'
    PERMOTATIONS = 500
    IS_PRINT_OUTPUTS= True
    SEE_STDERR = True

    @classmethod
    def number2(cls): return random.randrange(1, 30)

    @classmethod
    def number3(cls): return random.randrange(1,20)

    def data_creator(self):
        len1 = self.number3()
        s = str(len1)
        s += '\n'
        s += str(self.number3())
        for i in range(1, len1):
            s+= ' ' + str(self.number3())
        return s

if __name__ == '__main__':
    #if not Test_spec().unit_test('11\n17 59 34 57 17 23 67 1 18 2 59', b'1\n'):
        #print('error')
        #sys.exit()
    if not Test_spec().unit_test('8\n18 6 17 15 10 18 8 7', b'1\n'):
        print('error2')
        sys.exit()
    Test_spec().main()
