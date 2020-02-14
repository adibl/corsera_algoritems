"""
min heap implumentation
"""
import pytest


class MinHeap(object):
    def __init__(self, arr=None):
        if arr == None:
            self.arr = []
        else:
            self.arr = arr

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def shift_up(self, i):
        while i > 0 and self.camp(self.arr[self.get_parent(i)], self.arr[i]) > 0:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

    def shift_down(self, i):
        while i < len(self.arr):
            min_value_index = None
            if self.get_left_child(i) < len(self.arr):
                min_value_index = self.get_left_child(i)
            if self.get_right_child(i) < len(self.arr):
                if self.camp(self.arr[self.get_right_child(i)], self.arr[min_value_index]) < 0:
                    min_value_index = self.get_right_child(i)
            if min_value_index is not None and self.camp(self.arr[min_value_index], self.arr[i]) < 0:
                self.swap(i, min_value_index)
                i = min_value_index
            else:
                return

    def add(self, item):
        self.arr.append(item)
        self.shift_up(len(self.arr) - 1)

    def get_min(self):
        return self.arr[0]

    def remove_min(self):
        ret = self.get_min()
        last_index = len(self.arr) - 1
        self.swap(0, last_index)
        del self.arr[-1]
        self.shift_down(0)
        return ret

    def __len__(self):
        return self.arr.__len__()

    def __str__(self):
        return list([var.__str__() for var in self.arr]).__str__()

    def change_priority(self, i, new_value):
        if self.camp(self.arr[i], new_value) < 0:
            self.arr[i] = new_value
            self.shift_down(i)
        else:
            self.arr[i] = new_value
            self.shift_up(i)

    def camp(self, one, other):
        return one - other


def test_heap_general():
    h = MinHeap()
    h.add(5)
    h.add(7)
    assert h.get_min() == 5
    h.add(3)
    assert h.remove_min() == 3
    assert h.remove_min() == 5
    assert h.remove_min() == 7


def test_len():
    h = MinHeap()
    h.add(7)
    h.add(5)
    h.add(3)
    assert len(h) == 3


def test_alot():
    h = MinHeap()
    for i in range(7):
        h.add(i)
    assert h.get_min() == 0
    assert h.remove_min() == 0
    assert h.remove_min() == 1
    assert h.remove_min() == 2
    assert h.remove_min() == 3


def test_cahnge_priority():
    h = MinHeap()
    h.add(5)
    h.add(7)
    h.add(9)
    h.add(1)
    print(h)
    h.change_priority(0, 12)
    assert h.get_min() == 5
    h.change_priority(len(h) - 1, 1)
    assert h.get_min() == 1
