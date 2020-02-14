import random
import numpy


class Node(object):
    @staticmethod
    def add(node, value, data=None):
        root = node
        if node is None:
            return Node(value, data)
        while node.pointer is not None:
            if node.identifier == value:
                node.data = data
                return root
            node = node.pointer
        if node.identifier == value:
            node.data = data
        else:
            root = Node(value, data, root)
        return root

    @staticmethod
    def find(node, value):
        while node is not None:
            if node.identifier == value:
                return node.data
            node = node.pointer
        return None

    @staticmethod
    def is_value(node, value):
        while node is not None:
            if node.identifier == value:
                return True
            node = node.pointer
        return False

    @staticmethod
    def delete(node, value):
        root = node
        if root is None:
            return None
        if root.identifier == value:
            root = root.pointer
            return root
        if node.pointer is not None:
            prev_node = node
            node = node.pointer
            while node is not None:
                if node.identifier == value:
                    prev_node.pointer = node.pointer
                    return root
                prev_node = node
                node = node.pointer
        return root

    def __init__(self, value, data=None, pointer=None):
        self.identifier = value
        self.pointer = pointer
        self.data = data

    def get_value(self):
        return self.identifier


class HashTable(object):
    PRIME = 16769023
    M = 10 ** 4
    @classmethod
    def IntHashFamily(cls):
        a = random.randrange(1, cls.PRIME)
        b = random.randrange(0, cls.PRIME)
        return lambda number: ((a * number + b) % cls.PRIME) % cls.M

    def __init__(self, hash_function=None):
        self.arr = numpy.empty((self.M), dtype=list)
        if hash_function is None:
            self.hash_function = self.IntHashFamily()
        else:
            self.hash_function = hash_function

    def get(self, value):
        pointer = self.hash_function(value)
        return Node.find(self.arr[pointer], value)

    def add(self, value, data=None):
        pointer = self.hash_function(value)
        self.arr[pointer] = Node.add(self.arr[pointer], value, data)

    def remove(self, value):
        pointer = self.hash_function(value)
        self.arr[pointer] = Node.delete(self.arr[pointer], value)

    def is_value(self, value):
        pointer = self.hash_function(value)
        return Node.is_value(self.arr[pointer], value)


def test_basic_find():
    h = HashTable()
    h.add(543, 'a')
    h.add(321, 'b')
    assert h.get(543) == 'a'
    assert h.get(321) == 'b'
    h.remove(543)
    assert h.get(543) is None


def test_hash_stability():
    h = HashTable()
    func = h.IntHashFamily()
    assert func(123) == func(123)


def test_get_not_fond():
    h = HashTable()
    assert h.get(345) is None


def test_remove_not_fond():
    h = HashTable()
    h.remove(345)


def test_rewrite():
    h = HashTable()
    h.add(345, 'one')
    assert h.get(345) == 'one'
    h.add(345, 'three')
    assert h.get(345) == 'three'


def test_remove():
    HashTable.M = 1
    h = HashTable()
    h.add(12345, 'a')
    h.add(123456, 'b')
    assert h.is_value(12345) == True
    assert h.is_value(123456) == True
    h.remove(12345)
    assert h.get(12345) is None


def test_many_chain():
    HashTable.M = 1
    h = HashTable()
    for i in range(100):
        h.add(i)
    for i in range(100):
        assert h.is_value(i) is True
    for i in range(150, 170):
        assert h.is_value(i) is False
    for i in range(50):
        h.remove(i)
    for i in range(51, 100):
        assert h.is_value(i) is True
    for i in range(140, 160):
        h.add(i)
    for i in range(140, 160):
        assert h.is_value(i) is True


def test_remove():
    HashTable.M = 1
    h = HashTable()
    h.add(12345, 'a')
    h.add(123456, 'b')
    assert h.is_value(12345) == True
    assert h.is_value(123456) == True
    h.remove(12345)
    assert h.get(12345) is None
