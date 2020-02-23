from functools import total_ordering
import pytest
@total_ordering
class TreeNode(object):

    def __init__(self, value, parent=None):
        self.value = value
        self._parent = parent
        self._right_child = None
        self._left_child = None

    def __eq__(self, other):
        if type(other) is TreeNode:
            return self.value == other.value
        elif type(other) is type(self.value):
            return self.value == other
        else:
            raise NotImplementedError

    def __lt__(self, other):
        if type(other) is TreeNode:
            return self.value < other.value
        elif type(other) is type(self.value):
            return self.value < other
        else:
            raise NotImplementedError

    def __delete__(self):
        if self is self.parent.right_child:
            self.parent.right_child = None
        elif self is self.parent.left_child:
            self.parent.left_child = None
        self.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if self._parent is not None:
            if self._parent.right_child is self:
                self._parent.right_child = None
            elif self._parent.left_child is self:
                self._parent.left_child = None
        self._parent = value
        if self._parent is not None:
            if self > self._parent:
                self._parent.left_child = self
            else:
                self._parent.right_child = self

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, value):
        self._right_child = value
        if value is not None:
            value._parent = self

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, value):
        self._left_child = value
        if value is not None:
            value._parent = self

    def is_leaf(self):
        return self.right_child is None and self.left_child is None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def remove_leaf(self, node):
        if node.is_leaf():
            if node._parent.left_child is node:
                node._parent.left_child = None
            elif node._parent.right_child is node:
                node._parent.right_child = None
        else:
            raise NotImplementedError

    def right_ancestor(self, node):
        while node < node._parent:
            node = node._parent
        return node

    def left_descendant(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def next_in_size(self, node):
        if node.right_child is not None:
            return self.left_descendant(node.right_child)
        else:
            return self.right_ancestor(node)

    def get_biggest(self):
        node = self.root
        while node.left_child is not None:
            node = node.left_child
        return node

    def premote(self, node):
        if node.parent is self.root:
            self.root = node
        node.parent = node.parent.parent

    def switch(self, node, node2):
        if node is self.root:
            self.root = node2
        elif node2 is self.root:
            self.root = node
        node.parent, node2.parent = node2.parent, node.parent
        node.right_child, node2.right_child = node2.right_child, node.right_child
        node.left_child, node2.left_child = node2.left_child, node.left_child

    def find(self, data):
        node = self.root
        while node is not None:
            if data > node:
                if node.left_child is None:
                    return node
                node = node.left_child
            elif data < node:
                if node.right_child is None:
                    return node
                node = node.right_child

            else:
                return node
        return None

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            place = self.find(data)
            if data > place:
                place.left_child = TreeNode(data)
                place = place.left_child
            elif data < place:
                place.right_child = TreeNode(data)
                place = place.right_child
            return place

    def delete(self, data):
        if self.root is not None:
            node_to_delete = self.find(data)
            if node_to_delete.is_leaf():
                self.remove_leaf(node_to_delete)
            if node_to_delete.right_child is None:
                node_to_delete.left_child.parent = node_to_delete.parent
                ret = node_to_delete.value
                del node_to_delete
                return ret
            else:
                replace_node = self.next_in_size(node_to_delete)
                self.switch(replace_node, node_to_delete)
                if node_to_delete.right_child is not None:
                    self.premote(node_to_delete.right_child)
                ret = node_to_delete.value
                self.remove_leaf(node_to_delete)
                return ret

    def get_in_order(self):
        return self.get_in_order_recursion(self.root)

    def get_in_order_recursion(self, root):
        if root is None:
            return []
        return self.get_in_order_recursion(root.right_child) + [root.value, ] + self.get_in_order_recursion(root.left_child)

    def get_pre_order(self):
        return self.get_pre_order_recursion(self.root)

    def get_pre_order_recursion(self, root):
        if root is None:
            return []
        return [root.value, ] + self.get_pre_order_recursion(root.right_child) + self.get_pre_order_recursion(root.left_child)

    def get_post_order(self):
        return self.get_post_order_recursion(self.root)

    def get_post_order_recursion(self, root):
        if root is None:
            return []
        return self.get_post_order_recursion(root.right_child) + self.get_post_order_recursion(root.left_child) + [root.value, ]


def test_Node_parameters():
    n1 = TreeNode('fff')
    n2 = TreeNode('abc')
    n1.right_child = n2
    assert n2.parent is n1


def test_node_delete():
    n1 = TreeNode('1')
    n1.right_child = TreeNode('2')
    n1.right_child.right_child = TreeNode('3')
    n2 = n1.right_child
    del n2
    n1.right_child is None


def test_compare():
    n1 = TreeNode(12)
    n2 = TreeNode(10)
    assert n1 > n2
    assert not n1 == n2


def test_tree_add():
    tree = BinaryTree()
    tree.add(12)
    tree.add(5)
    tree.add(6)
    assert tree.root.left_child is None


def test_tree_find():
    tree = BinaryTree()
    tree.add(12)
    tree.add(7)
    tree.add(15)
    assert tree.find(15).parent is tree.root


def test_tree_find_not_precise():
    tree = BinaryTree()
    tree.add(12)
    tree.add(7)
    tree.add(15)
    assert tree.find(14) == 15
    assert tree.find(11) == 7
    assert tree.find(4) == 7


def test_tree_delete_near():
    tree = BinaryTree()
    tree.add(12)
    tree.add(7)
    tree.add(15)
    tree.delete(12)
    assert tree.find(7) == 7
    assert tree.find(15) == 15
    assert tree.find(12) == 15
    assert tree.root == 7
    assert tree.root.left_child == 15
    assert tree.root.right_child is None


def test_delete_far():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(3)
    tree.add(2)
    tree.delete(5)
    assert tree.find(5) == 3
    assert tree.find(2) == 2


def test_delete_far2():
    tree = BinaryTree()
    tree.add(2)
    tree.add(3)
    tree.add(5)
    tree.add(10)
    tree.delete(5)
    assert tree.find(5) == 10
    assert tree.find(2) == 2


def test_get_in_order():
    tree = BinaryTree()
    tree.add(4)
    tree.add(2)
    tree.add(5)
    tree.add(3)
    tree.add(1)
    assert tree.get_in_order() == [1, 2, 3, 4, 5]


def test_get_pre_order():
    tree = BinaryTree()
    tree.add(4)
    tree.add(2)
    tree.add(5)
    tree.add(3)
    tree.add(1)
    assert tree.get_pre_order() == [4, 2, 1, 3, 5]


def test_get_post_order():
    tree = BinaryTree()
    tree.add(4)
    tree.add(2)
    tree.add(5)
    tree.add(3)
    tree.add(1)
    assert tree.get_post_order() == [1, 3, 2, 5, 4]
