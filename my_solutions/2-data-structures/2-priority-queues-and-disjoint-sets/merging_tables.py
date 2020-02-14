import numpy


class DisjoinSet(object):
    def __init__(self, max_number, ranks=None, sets=None):
        if sets == None:
            self.sets = numpy.zeros(max_number, dtype=int)
        else:
            self.sets = sets
        if ranks == None:
            self.sizes = numpy.zeros(max_number, dtype=int)
            self.max_size = 0
        else:
            self.sizes = ranks
            self.max_size = max(ranks)

    def make_set(self, number):
        self.sets[number] = number
        self.sizes[number] = 1

    def find(self, number):
        if self.sets[number] == number:
            return number
        else:
            root = self.find(self.sets[number])
            self.sets[number] = root
            return root

    def union(self, number1, number2):
        root1 = self.find(number1)
        root2 = self.find(number2)
        if root1 != root2:
            if self.sizes[root1] > self.sizes[root2]:
                self.sets[root2] = root1
                self.sizes[root1] += self.sizes[root2]
                if self.sizes[root1] > self.max_size:
                    self.max_size = self.sizes[root1]
            else:
                self.sets[root1] = root2
                self.sizes[root2] += self.sizes[root1]
                if self.sizes[root2] > self.max_size:
                    self.max_size = self.sizes[root2]

    def get_max_size(self):
        return self.max_size


number_of_tables, number_of_lines = [int(x) for x in input().split()]
ranks = [int(x) for x in input().split()]
disjoinset = DisjoinSet(number_of_tables, ranks, list(range(number_of_tables)))
to_print = []
for line in range(number_of_lines):
    set1, set2 = [int(x) - 1 for x in input().split()]
    disjoinset.union(set1, set2)
    to_print.append(disjoinset.get_max_size())

for var in to_print:
    print(var)
