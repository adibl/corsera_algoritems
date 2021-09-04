# Uses python3
import random

from test_class import Test

import sys
sys.setrecursionlimit(10**4)


class Test_spec(Test):
    COURSE_PATH = '/solutions/3-algorithms-on-graphs/2-decomposition-2/strongly_connected.py'
    MY_PATH = "/my_solutions/3-algorithms-on-graphs/2-decomposition-2/strongly_connected.py"
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    PERMOTATIONS = 100
    TIME_LIMIT = 5
    IDE = False

    @classmethod
    def node_number(cls):
        return random.randint(2, 10000)

    @classmethod
    def conn_value(cls, v):
        nums = [0, 0]
        while nums[0] == nums[1]:
            nums = [random.randint(1, v), random.randint(1, v)]
        return nums

    def create_grath(self, v, e):
        return [self.conn_value(v) for _ in range(e)]

    def data_creator(self):
        v = self.node_number()
        e = self.node_number()
        cons = self.create_grath(v, e)

        s = "{} {}\n".format(v, e)
        string_cons = ["{} {}".format(*[x for x in con]) for con in cons]
        s += "\n".join(string_cons) + '\n'
        return s
