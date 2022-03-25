from typing import List, Optional
from structures import TreeNode, binaryTree

class Solution:

    bt = binaryTree()

    def sortedArrayToBST(self, lst: List[int]) -> Optional[TreeNode]:
        print(lst)
        if not lst:
            return []
        root = self.bt.sorted_array_to_bst(lst)
        return self.bt.make_lst_by_bst(root, len(lst))

if __name__ == "__main__":
    s = Solution()

    s.sortedArrayToBST(lst=[-10, -7, -3, 0, 5, 7, 9])
    # assert s.sortedArrayToBST(lst=[-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5]
    # assert s.sortedArrayToBST(lst=[-10, -7, -3, -1, 0, 1, 4, 5, 7, 9]) == [1, -3, 7, -7, 0, 5, 9, -10, None, -1, None]