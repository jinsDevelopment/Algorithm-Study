from typing import List


class Solution:
    # 바이러스
    def virus(self):
        n = int(input())
        m = int(input())
        graph = [[] * n for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        self.cnt = 0
        visited = [0] * (n + 1)

        def dfs(start):
            visited[start] = 1
            for i in graph[start]:
                if visited[i] == 0:
                    dfs(i)
                    self.cnt += 1

        dfs(1)

        return self.cnt

if __name__ == "__main__":
    s = Solution()

    # node = 7
    # edge = 6
    # array = [
    #     [1, 2],
    #     [2, 3],
    #     [1, 5],
    #     [5, 2],
    #     [5, 6],
    #     [4, 7],
    #     ]

    print(s.virus())
