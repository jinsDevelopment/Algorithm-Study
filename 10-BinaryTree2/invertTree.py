from structures import TreeNode, binaryTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    bt = binaryTree()

    def invertTree(self, lst: TreeNode) -> TreeNode:
        if not lst:
            return []

        def invert(parent):
            if parent:
                parent.left, parent.right = invert(parent.right), invert(parent.left)
                return parent

        root = self.bt.make_tree_by(lst, 0)
        return self.bt.make_lst_by(invert(root))

if __name__ == "__main__":

    s = Solution()

    assert s.invertTree(lst=[]) == []
    assert s.invertTree(lst=[2]) == [2]
    assert s.invertTree(lst=[2, 1, 3, 5, 6, 2, 3]) == [2, 3, 1, 3, 2, 6, 5]
    assert s.invertTree(lst=[4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1]