#Uses python3
import random

from test_class import Test


class Test_spec(Test):
    COURSE_PATH = '/solutions/3-algorithms-on-graphs/1-decomposition-1/connectedComponents.py'
    MY_PATH = "/my_solutions/3-algorithms-on-graphs/1-decomposition-1/connected_components.py"
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    PERMOTATIONS = 100
    TIME_LIMIT = 5

    @classmethod
    def node_number(cls):
        return random.randint(2, 1000)

    @classmethod
    def conn_value(cls, v):
        nums = [0, 0]
        while nums[0] == nums[1]:
            nums = [random.randint(1, v), random.randint(1, v)]
        return nums

    def data_creator(self):
        v = self.node_number()
        e = self.node_number()
        cons = [self.conn_value(v) for i in range(e)]
        s = "{} {}\n".format(v, e)
        string_cons = ["{} {}".format(*con) for con in cons]
        s += "\n".join(string_cons) + '\n'
        return s


def test_basic_grath():
    test = Test_spec()
    assert test.unit_test('4 2\n1 2\n3 2') == '2'
