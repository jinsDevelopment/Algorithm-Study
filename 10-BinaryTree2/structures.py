from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class binaryTree:

    def make_tree_by(self,lst, idx):
        parent = None
        if idx < len(lst):
            value = lst[idx]
            if value == None:
                return

            parent = TreeNode(value)
            parent.left = self.make_tree_by(lst, 2 * idx + 1)
            parent.right = self.make_tree_by(lst, 2 * idx + 2)

        return parent

    def sorted_array_to_bst(self, lst: List[int]):
        print(lst)
        if not lst:
            return None

        mid = len(lst) // 2
        node = TreeNode(lst[mid])
        node.left = self.sorted_array_to_bst(lst[:mid])

        node.right = self.sorted_array_to_bst(lst[mid + 1:])


        return node

    # None 처리
    def make_lst_by_bst(self,root, limit):

        if not root:
            return []

        lst = []
        q = deque([root])

        while q:
            if len(lst) > limit:
                break

            node = q.popleft()
            if node:
                lst.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                lst.append(None)

        return lst

    # None 미처리
    def make_lst_by(self,root):
        if not root:
            return []

        lst = []
        q = deque([root])

        while q:
            node = q.popleft()
            lst.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return lst


if __name__ == "__main__":
    bt = binaryTree()

