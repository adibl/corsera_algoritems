import random
from tests import Test


class TestAlgo(Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/1-algorithmic-toolbox/3-greedy-algorithms/'
    FILE_NAME = 'carFueling.py'
    PERMOTATIONS = 1000

    def data_creator(self):
        d = random.randrange(1, 10 ** 5)
        m = random.randrange(1, 400)
        n = random.randrange(1, 3)
        s = str(d) + '\r\n' + str(m) + '\r\n' + str(n) + '\r\n'
        arr = []
        for i in range(0, n):
            arr.append(random.randrange(1, d))
        arr = sorted(arr)
        s += str(arr[0])
        for i in range(1, n):
            s += ' ' + str(arr[i])
        s += '\r\n'
        return s


if __name__ == '__main__':
    TestAlgo().main()
