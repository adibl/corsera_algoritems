#Uses python3
import random

from win_test_class import Test
import networkx as nx
from networkx.generators.random_graphs import erdos_renyi_graph

class Test_spec(Test):
    COURSE_PATH = '\\solutions\\3-algorithms-on-graphs\\2-decomposition-2\\acyclicity.py'
    MY_PATH = "\\my_solutions\\3-algorithms-on-graphs\\2-decomposition-2\\acyclicity.py"
    #IS_PRINT_OUTPUTS = True
    #SEE_STDERR = True
    PERMOTATIONS = 100
    TIME_LIMIT = 5
    G = None

    @classmethod
    def node_number(cls):
        return random.randint(2, 1000)

    def data_creator(self):
        self.G = nx.gnp_random_graph(self.node_number(), 0.5, directed=True)
        # DAG = nx.DiGraph([(u, v,) for (u, v) in G.edges() if u < v])
        nodes = self.G.nodes
        edges = self.G.edges
        s = "{} {}\n".format(len(nodes), len(edges))
        string_cons = ["{} {}".format(*[x + 1 for x in con]) for con in edges]
        s += "\n".join(string_cons) + '\n'
        return s