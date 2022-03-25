from typing import List
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(elements, start, k):

            if k == 0:
                result.append(elements[:])
                return

            for num in range(start, n+1):
                elements.append(num)
                dfs(elements, num + 1, k -1)
                elements.pop()

        dfs([],1,k)
        return result



    def combinePythonBook(self, n: int, k: int) -> List[List[int]]:
            return list(itertools.combinations(range(1, n + 1), k))






if __name__ == "__main__":
    s = Solution()

    print(s.combine(4,2))
    print(s.combinePythonBook(4,2))