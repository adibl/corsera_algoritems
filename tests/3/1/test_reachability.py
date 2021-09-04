#Uses python3
import random

from test_class import Test


class Test_spec(Test):
    COURSE_PATH = '/solutions/3-algorithms-on-graphs/1-decomposition-1/reachability.py'
    MY_PATH = "/my_solutions/3-algorithms-on-graphs/1-decomposition-1/reachability.py"
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    PERMOTATIONS = 1000
    TIME_LIMIT = 5

    @classmethod
    def node_number(cls):
        return random.randint(2, 2000)

    @classmethod
    def conn_value(cls, v):
        nums = [0, 0]
        while nums[0] == nums[1]:
            nums = [random.randint(1, v), random.randint(1, v)]
        return nums

    def data_creator(self):
        v = self.node_number()
        e = self.node_number()
        cons = [self.conn_value(v) for i in range(e + 1)]
        s = "{} {}\n".format(v, e)
        string_cons = ["{} {}".format(*con) for con in cons]
        s += "\n".join(string_cons) + '\n'
        return s


def test_basic_grath():
    test = Test_spec()
    assert test.unit_test('4 4\n1 2\n3 2\n4 3\n1 4\n1 4\n') == '1'
    assert test.unit_test('4 2\n1 2\n3 2\n1 4\n') == '0'

def test_oposit_conn():
    test = Test_spec()
    assert test.unit_test('4 4\n1 2\n3 2\n4 3\n1 4\n4 1\n') == '1'
