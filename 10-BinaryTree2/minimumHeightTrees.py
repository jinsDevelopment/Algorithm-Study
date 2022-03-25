from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        dic = defaultdict(list)

        for i, j in edges:
            dic[i].append(j)
            dic[j].append(i)

        leaves = []
        for i in range(n + 1):
            if len(dic[i]) == 1:
                leaves.append(i)











if __name__ == "__main__":
    s = Solution()

    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(s.findMinHeightTrees(n, edges))