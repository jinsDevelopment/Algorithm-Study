from structures import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest:int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def dfs(node:TreeNode):
            if not node:
                return -1
            print(node.val)
            # 왼쪽, 오른쪽 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태 값
            return max(left, right) + 1

        dfs(root)

        return self.longest



if __name__ == "__main__":
    s = Solution()

    # array = [1, 2, 3, 4, 5]
    e = TreeNode(5)
    d = TreeNode(4)
    c = TreeNode(3)
    b = TreeNode(2,d,e)
    a = TreeNode(1,b,c)

    print(s.diameterOfBinaryTree(a))

