from structures import TreeNode, binaryTree
from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    bt = binaryTree()

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        lst = self.bt.make_tree_by(root, 0)

        def dfs(lst):

            if not lst:
                return 0

            left = dfs(lst.left)
            right = dfs(lst.right)

            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left , right) + 1

        return dfs(lst) != -1





if __name__ == "__main__":
    s = Solution()

    array = [3, 9, 20, None, None, 15, 7]
    print(s.isBalanced(array))
    array = [1,2,2,3,3,None,None,4,4]
    print(s.isBalanced(array))

