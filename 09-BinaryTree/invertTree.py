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

    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = deque([root])

        while stack:
            node = stack.pop()

            if node:

                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root






if __name__ == "__main__":
    s = Solution()

    array = [4, 2, 7, 1, 3, 6, 9]

    a = TreeNode(4, TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(7,TreeNode(6),TreeNode(9)))


    # res = s.invertTree(a)
    #
    # # preorder 출력
    # def dfs(res):
    #     while res:
    #         print(res.val)
    #         if res:
    #             dfs(res.left)
    #             dfs(res.right)
    #
    #         return None
    #
    # dfs(res)


