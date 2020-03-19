from splay_tree import SplayTree
from binary_tree import TreeNode


class TreeNodeWithSum(TreeNode):
    def __init__(self, value, parent=None):
        super().__init__(value, parent)
        self._subtree_sum = value

    @property
    def subtree_sum(self):
        return self._subtree_sum

    @subtree_sum.setter
    def subtree_sum(self, value):
        self._subtree_sum = value


class SplayTreeWithSum(SplayTree):
    def _add_no_splay(self, value):
        if self.root is None:
            self.root = TreeNodeWithSum(value)
            return self.root
        else:
            node = super()._find_dont_splay(value)
            if value > node:
                node.right_child = TreeNodeWithSum(value)
                node.subtree_sum += value
                node = node.right_child
            elif value < node:
                node.left_child = TreeNodeWithSum(value)
                node.subtree_sum += value
                node = node.left_child
            return node

    def _zig(self, node: TreeNodeWithSum):
        super()._zig(node)
        self.update_subtree_sum(node.right_child)
        self.update_subtree_sum(node.left_child)
        self.update_subtree_sum(node)

    def _zag(self, node):
        super()._zag(node)
        self.update_subtree_sum(node.right_child)
        self.update_subtree_sum(node.left_child)
        self.update_subtree_sum(node)

    @staticmethod
    def update_subtree_sum(node):
        if node is None:
            return
        node.subtree_sum = node.value
        if node.left_child is not None:
            node.subtree_sum += node.left_child.subtree_sum
        if node.right_child is not None:
            node.subtree_sum += node.right_child.subtree_sum

    @staticmethod
    def merge(tree1, tree2):
        tree = SplayTree.merge(tree1, tree2)
        SplayTreeWithSum.update_subtree_sum(tree.root)
        return tree

    def split(self, value, root_in_min_tree: bool):
        tree1, tree2 = super().split(value, root_in_min_tree)
        self.update_subtree_sum(tree1.root)
        self.update_subtree_sum(tree2.root)
        return tree1, tree2


if __name__ == "__main__":
    x = 0
    m = 1000000001
    num_of_lines = int(input())
    tree = SplayTreeWithSum()
    for _ in range(num_of_lines):
        line = input().split()
        operator = line[0]
        numbers = [(int(var) + x) % m for var in line[1:]]
        if operator == '+':
            tree.add(numbers[0])
        elif operator == '-':
            tree.delete(numbers[0])
        elif operator == '?':
            node = tree.find(numbers[0])
            if node == numbers[0]:
                print("Found")
            else:
                print("Not found")
        elif operator == 's': 
            befor_sum, with_sum = tree.split(numbers[0], False)
            tree_sum, after_sum = with_sum.split(numbers[1], True)
            if tree_sum.root is None:
                numbers_sum = 0
            else:
                numbers_sum = tree_sum.root.subtree_sum
            with_sum = SplayTreeWithSum.merge(befor_sum, tree_sum)
            tree = SplayTreeWithSum.merge(with_sum, after_sum)
            print(str(numbers_sum))
            x = numbers_sum
