import pytest
import random
import string
import sys
import test_class


class Test_spec(test_class.Test):
    COURSE_PATH = '/home/adi/PycharmProjects/algoritems/solutions/2-data-structures/1-basic-data-structures/'
    MY_PATH = '/home/adi/PycharmProjects/algoritems/my_solutions/2-data-structures/1-basic-data-structures/'
    FILE_NAME = 'treeHeight.py'
    PERMOTATIONS = 50
    TIME_LIMIT = 3.0

    @classmethod
    def number(cls): return random.randrange(1,10 ** 5)

    def create_tree(self, roots, empty_indexes, arr):
        node_num_in_level = random.randint(len(roots), len(roots) * 1000)
        next_roots = []
        for node in range(node_num_in_level):
            if len(empty_indexes) > 0:
                num = random.choice(empty_indexes)
                arr[num] = random.choice(roots)
                next_roots.append(num)
                empty_indexes.remove(num)
        if len(empty_indexes) > 0:
            self.create_tree(next_roots, empty_indexes, arr)


    def data_creator(self):
        len1 = self.number()
        s = str(len1) + '\r\n'
        empty_indexes = [x for x in range(len1)]
        arr = [-2 for x in range(len1)]
        num = random.choice(empty_indexes)
        arr[num] = -1
        empty_indexes.remove(num)
        self.create_tree([num], empty_indexes, arr)
        assert len(empty_indexes) == 0
        s +=  ' '.join([str(x) for x in arr])
        return s

if __name__ == '__main__':
    test = Test_spec()
    test.main()

def test_my_only():
    test = Test_spec()
    assert test.unit_test('5\n4 -1 4 1 1', "b'3\\n'") == True
    assert test.unit_test('5\n-1 0 4 0 3', "b'4\\n'") == True



