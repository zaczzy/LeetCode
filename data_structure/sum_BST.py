# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# used in range_sum_BST.py
class SumTree:
    def __init__(self, root):
        self.root = root
        self.sums = dict()

    def get_sum(self, node):
        if node.val not in self.sums:
            if not node.left and not node.right:
                self.sums[node.val] = node.val
            elif not node.left:
                self.sums[node.val] = self.get_sum(node.left) + node.val
            elif not node.right:
                self.sums[node.val] = self.get_sum(node.right) + node.val
            else:
                self.sums[node.val] = self.get_sum(node.right) + self.get_sum(node.right) + node.val
            return self.sums[node.val]
        else:
            return self.sums[node.val]
