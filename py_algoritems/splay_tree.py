from binary_tree import BinaryTree, TreeNode


class SplayTree(BinaryTree):

    @staticmethod
    def merge(tree1, tree2):
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

    def add_no_splay(self, vlaue):
        super().add(vlaue)

    def add(self, value):
        node = super().add(value)
        self.splay(node)

    def zig(self, node: TreeNode):
        parent = node.parent
        is_right_zig = parent.right_child is node
        node_right = node.right_child
        node_left = node.left_child
        if parent is self.root:
            self.root = node
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

    def zag(self, node):
        parent = node.parent
        is_right_zag = parent.right_child is node
        if parent is self.root:
            self.root = node
        else:
            node.parent = parent.parent
        if is_right_zag:
            parent.right_child = node.left_child
            node.left_child = parent
        else:
            parent.left_child = node.right_child
            node.right_child = parent

    def zigzag(self, node):
        self.zig(node)
        self.zag(node)

    def zigzig(self, node):
        self.zig(node)
        self.zig(node)

    def splay(self, node):
        while node is not self.root:
            if self.root is node.parent:
                self.zig(node)
            else:
                is_node_right = node.parent.right_child is node
                is_parent_right = node.parent.parent.right_child is node.parent
                if is_node_right != is_parent_right:
                    self.zigzag(node)
                else:
                    self.zigzig(node)


def test_zig_left():
    t = SplayTree()
    t.add_no_splay(10)
    t.add_no_splay(5)
    t.add_no_splay(7)
    t.add_no_splay(2)
    t.add_no_splay(17)
    t.zig(t.root.left_child)
    assert t.root == 5
    assert t.root.right_child == 10
    assert t.root.right_child.right_child == 17
    assert t.root.right_child.left_child == 7
    assert t.root.left_child == 2


def test_zig_right():
    t = SplayTree()
    t.add_no_splay(10)
    t.add_no_splay(5)
    t.add_no_splay(7)
    t.add_no_splay(2)
    t.add_no_splay(17)
    t.zig(t.root.left_child)
    t.zig(t.root.right_child)
    assert t.root == 10
    assert t.root.right_child == 17
    assert t.root.left_child == 5
    assert t.root.left_child.left_child == 2
    assert t.root.left_child.right_child == 7


def test_zigzag_right():
    t = SplayTree()
    t.add_no_splay(10)
    t.add_no_splay(17)
    t.add_no_splay(5)
    t.add_no_splay(4)
    t.add_no_splay(7)
    t.add_no_splay(6)
    t.add_no_splay(8)
    t.zigzag(t.root.left_child.right_child)
    assert t.root == 7
    assert t.root.left_child == 5
    assert t.root.left_child.left_child == 4
    assert t.root.left_child.right_child == 6
    assert t.root.right_child == 10
    assert t.root.right_child.left_child == 8
    assert t.root.right_child.right_child == 17


def test_splay():
    t = SplayTree()
    t.add_no_splay(10)
    t.add_no_splay(11)
    t.add_no_splay(12)
    t.add_no_splay(13)
    t.splay(t.root.right_child.right_child.right_child)
    assert t.root == 13


def test_merge():
    t1 = SplayTree()
    t1.add_no_splay(5)
    t1.add_no_splay(7)
    t2 = SplayTree()
    t2.add_no_splay(2)
    t2.add_no_splay(3)
    t_result = SplayTree.merge(t1, t2)
    assert t_result.root == 3
    assert t_result.root.left_child == 2
    assert t_result.root.right_child == 5
    assert t_result.root.right_child.right_child == 7


def test_delte():
    t = SplayTree()
    t.add_no_splay(10)
    t.add_no_splay(17)
    t.add_no_splay(5)
    t.add_no_splay(4)
    t.add_no_splay(7)
    t.delete(t.root.left_child.right_child)
    assert t.root == 5
    assert t.root.right_child == 10
    assert t.root.right_child.right_child == 17
    assert t.root.left_child == 4
