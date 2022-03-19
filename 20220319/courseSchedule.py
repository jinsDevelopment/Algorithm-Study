from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)

        # 그래프 순서대로 구성
        for a, b in sorted(prerequisites):
            dic[a].append(b)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)

            for y in dic[i]:

                if not dfs(y):
                    return False

            traced.remove(i)

            visited.add(i)

            return True

        for x in list(dic):

            if not dfs(x):
                return False

        return True


if __name__ == "__main__":
    s = Solution()

    # numCourses = 2
    # prerequisites = [[1, 0]]
    #
    # print(s.canFinish(numCourses, prerequisites))

    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(s.canFinish(numCourses, prerequisites))
