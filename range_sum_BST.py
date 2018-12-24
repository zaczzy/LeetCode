from data_structure import sum_BST
class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum_tree = sum_BST.SumTree(root)
        rangeSum = 0
        curr = root
        while curr:
            if L <= curr.val <= R:
                pass
            elif curr.val < L:
                pass
            else:
                # curr.val > R
                pass
        return rangeSum
