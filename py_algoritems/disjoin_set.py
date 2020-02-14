"""
disjoin set implimentation
"""
import numpy


class DisjoinSet(object):
    def __init__(self, max_number):
        self.sets = numpy.zeros(max_number, dtype=int)
        self.ranks = numpy.zeros(max_number, dtype=int)

    def make_set(self, number):
        self.sets[number] = number
        self.ranks[number] = 1

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
        if self.ranks[root1] == self.ranks[root2]:
            self.sets[root2] = root1
            self.ranks[root1] += 1
        elif self.ranks[root1] > self.ranks[root2]:
            self.sets[root2] = root1
        else:
            self.sets[root1] = root2


def test_create():
    d = DisjoinSet(100)
    d.make_set(1)
    d.make_set(2)
    assert d.find(1) != d.find(2)


def test_union():
    d = DisjoinSet(100)
    d.make_set(1)
    d.make_set(2)
    d.union(1, 2)
    assert d.find(1) == d.find(2)


def test_find_path_compression():
    d = DisjoinSet(100)
    d.sets[1] = 1
    d.sets[2] = 1
    d.sets[3] = 2
    assert d.sets[3] != 1
    d.find(3)
    assert d.sets[3] == 1
