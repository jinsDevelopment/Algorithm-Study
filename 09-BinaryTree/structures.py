from collections import deque

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

    def test_max_depth(self,lst):
        root = self.make_tree_by(lst, 0)

        if not root:
            return 0

        q = deque([root])

        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                print(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth



if __name__ == "__main__":

    bt = binaryTree()

    assert bt.test_max_depth(lst=[]) == 0
    assert bt.test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3