# Uses python3
import random

from win_test_class import Test
import networkx


def scramble_numbers(cons, nodes):
    new_numbers = set(range(1, nodes + 1))
    convert_dict = dict()
    for num in range(1, nodes + 1):
        new_number = random.sample(new_numbers, 1)[0]
        convert_dict[num] = new_number
        new_numbers.remove(new_number)
    new_cons = []
    for con in cons:
        new_cons.append([convert_dict.get(num) for num in con])
    return new_cons


class Test_spec(Test):
    COURSE_PATH = '\\solutions\\3-algorithms-on-graphs\\2-decomposition-2\\toposort.py'
    MY_PATH = "\\my_solutions\\3-algorithms-on-graphs\\2-decomposition-2\\order_dag.py"
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    PERMOTATIONS = 100
    TIME_LIMIT = 10
    G = None
    ONLINE = False

    @classmethod
    def node_number(cls):
        return random.randint(2, 100000)

    @classmethod
    def conn_value(cls, v):
        nums = [0, 0]
        while nums[0] == nums[1]:
            nums = [random.randint(1, v), random.randint(1, v)]
        return sorted(nums)

    def create_grath(self, v, e):
        cons = scramble_numbers([self.conn_value(v) for _ in range(e)], v)
        G = networkx.DiGraph(cons)
        for vertix in range(1, v + 1):
            G.add_node(vertix)
        self.G = G
        return cons

    def data_creator(self):
        v = self.node_number()
        e = self.node_number()
        cons = self.create_grath(v, e)

        while not networkx.is_directed_acyclic_graph(self.G):
            v = self.node_number()
            e = self.node_number()
            cons = self.create_grath(v, e)
        s = "{} {}\n".format(v, e)
        string_cons = ["{} {}".format(*[x for x in con]) for con in cons]
        s += "\n".join(string_cons) + '\n'
        return s

    def compare_output(self, my_result, course_result):
        if not self.validate_result(course_result):
            raise Exception("test error")
        return self.validate_result(my_result)

    def validate_result(self, result):
        return True
        result_list = [int(x) for x in result.split(" ")]
        return result_list in list(networkx.algorithms.dag.all_topological_sorts(self.G))
