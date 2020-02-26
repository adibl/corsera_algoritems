from binary_tree import BinaryTree, TreeNode


class SplayTree(BinaryTree):
    @staticmethod
    def merge(tree1, tree2):
        if tree1.root is None:
            return tree2
        elif tree2.root is None:
            return tree1
        biggest1 = tree1.get_biggest()
        biggest2 = tree2.get_biggest()
        if biggest1 > biggest2:
            tree2.splay(biggest2)
            tree2.root.right_child = tree1.root
            return tree2
        else:
            tree1.splay(biggest1)
            tree1.root.right_child = tree2.root
            return tree1

    def split(self, value, root_in_min_tree: bool):
        """
        destroy the current tree, hardcopy in if ypu need it before
        """
        node = self.find(value)
        min_tree = type(self)()
        max_tree = type(self)()
        if node is not None:
            if node > value:
                root_in_min_tree = False
            elif node < value:
                root_in_min_tree = True
            if self.root is not None:
                if root_in_min_tree:
                    min_tree.root = node
                    max_tree.root = node.right_child
                    node.right_child = None
                else:
                    min_tree.root = node.left_child
                    max_tree.root = node
                    node.left_child = None
                self.root = None
        return min_tree, max_tree

    def _split_no_root(self, value):
        """
        destroy the current tree, hardcopy in if ypu need it before
        """
        node = self.find(value)
        self.splay(node)
        min_tree = SplayTree()
        max_tree = SplayTree()
        min_tree.root = node.left_child
        max_tree.root = node.right_child
        node.right_child = None
        node.left_child = None
        self.root = None
        return min_tree, max_tree

    def _add_no_splay(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            place = super().find(data)
            if data > place:
                place.right_child = TreeNode(data)
                place = place.right_child
            elif data < place:
                place.left_child = TreeNode(data)
                place = place.left_child
            return place

    def add(self, value):
        node = self._add_no_splay(value)
        self.splay(node)

    def find(self, value):
        node = self._find_dont_splay(value)
        if node is not None:
            self.splay(node)
        return node

    def _find_dont_splay(self, value):
        return super().find(value)

    def delete(self, value):
        node_to_delete = self._find_dont_splay(value)
        if node_to_delete != value:
            return node_to_delete
        nex_in_size = self.next_in_size(node_to_delete)
        if nex_in_size is not None:
            self.splay(nex_in_size)
        self.splay(node_to_delete)
        return super()._delete_node(node_to_delete)

    def _zig(self, node: TreeNode):
        parent = node.parent
        is_right_zig = parent.right_child is node
        node_right = node.right_child
        node_left = node.left_child
        if parent is self.root:
            self.root = node
            node.parent = None
        else:
            node.parent = parent.parent
        if is_right_zig:
            node.left_child = parent
            node.right_child = node_right
            parent.right_child = node_left
        else:
            node.left_child = node_left
            node.right_child = parent
            parent.left_child = node_right

    def _zag(self, node):
        parent = node.parent
        is_right_zag = parent.right_child is node
        if parent is self.root:
            self.root = node
            node.parent = None
        else:
            node.parent = parent.parent
        if is_right_zag:
            parent.right_child = node.left_child
            node.left_child = parent
        else:
            parent.left_child = node.right_child
            node.right_child = parent

    def _zigzag(self, node):
        self._zig(node)
        self._zag(node)

    def _zigzig(self, node):
        self._zig(node)
        self._zig(node)

    def splay(self, node):
        while node is not self.root:
            if self.root is node.parent:
                self._zig(node)
            else:
                is_node_right = node.parent.right_child is node
                is_parent_right = node.parent.parent.right_child is node.parent
                if is_node_right != is_parent_right:
                    self._zigzag(node)
                else:
                    self._zigzig(node)


def test_zig_left():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(5)
    t._add_no_splay(7)
    t._add_no_splay(2)
    t._add_no_splay(17)
    t._zig(t.root.left_child)
    assert t.root == 5
    assert t.root.right_child == 10
    assert t.root.right_child.right_child == 17
    assert t.root.right_child.left_child == 7
    assert t.root.left_child == 2


def test_zig_right():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(5)
    t._add_no_splay(7)
    t._add_no_splay(2)
    t._add_no_splay(17)
    t._zig(t.root.left_child)
    t._zig(t.root.right_child)
    assert t.root == 10
    assert t.root.right_child == 17
    assert t.root.left_child == 5
    assert t.root.left_child.left_child == 2
    assert t.root.left_child.right_child == 7


def test_zigzag_right():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(4)
    t._add_no_splay(7)
    t._add_no_splay(6)
    t._add_no_splay(8)
    t._zigzag(t.root.left_child.right_child)
    assert t.root == 7
    assert t.root.left_child == 5
    assert t.root.left_child.left_child == 4
    assert t.root.left_child.right_child == 6
    assert t.root.right_child == 10
    assert t.root.right_child.left_child == 8
    assert t.root.right_child.right_child == 17


def test_splay():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(11)
    t._add_no_splay(12)
    t._add_no_splay(13)
    t.splay(t.root.right_child.right_child.right_child)
    assert t.root == 13


def test_merge():
    t1 = SplayTree()
    t1._add_no_splay(5)
    t1._add_no_splay(7)
    t2 = SplayTree()
    t2._add_no_splay(2)
    t2._add_no_splay(3)
    t_result = SplayTree.merge(t1, t2)
    assert t_result.root == 3
    assert t_result.root.left_child == 2
    assert t_result.root.right_child == 5
    assert t_result.root.right_child.right_child == 7


def test_delete():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(4)
    t._add_no_splay(7)
    t.delete(7)
    assert t.root == 10
    assert t.root.right_child == 17
    assert t.root.left_child == 5
    assert t.root.left_child.left_child == 4


def test_split():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(4)
    t._add_no_splay(7)
    t1, t2 = t._split_no_root(7)
    assert t1.root == 5
    assert t1.root.left_child == 4
    assert t2.root == 10
    assert t2.root.right_child == 17


def test_split2():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(4)
    t._add_no_splay(7)
    t1, t2 = t.split(7, True)
    assert t1.root == 7
    assert t1.root.left_child == 5
    assert t2.root == 10
    assert t2.root.right_child == 17


def test_split3():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(4)
    t._add_no_splay(7)
    t1, t2 = t.split(5, False)
    assert t1.root == 4
    assert t2.root == 5
    assert t2.root.right_child == 10
    assert t2.root.right_child.left_child == 7

def test_split_not_in_tree():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(3)
    t._add_no_splay(7)
    t1, t2 = t.split(4, True)
    assert t1.root == 3
    assert t2.get_in_order() == [5, 7, 10, 17]

def test_split_not_in_tree_form_doun():
    t = SplayTree()
    t._add_no_splay(10)
    t._add_no_splay(17)
    t._add_no_splay(5)
    t._add_no_splay(3)
    t._add_no_splay(7)
    t1, t2 = t.split(6, True)
    assert t1.get_in_order() == [3, 5]
    assert t2.get_in_order() == [7, 10, 17]
