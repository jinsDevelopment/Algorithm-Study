class Solution:

    def __init__(self):
        self.graph = {
                        1: [2, 3, 4],
                        2: [5],
                        3: [5],
                        4: [],
                        5: [6, 7],
                        6: [],
                        7: [3],
                    }

    def dfs_recursive(self, node, visited):
        # 방문처리
        visited.append(node)

        # 인접 노드 방문
        for adj in self.graph[node]:
            if adj not in visited:
                self.dfs_recursive(adj, visited)

        return visited


    def dfs_stack(self, start):
        visited = []
        # 방문할 순서를 담아두는 용도
        stack = [start]

        # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
        while stack:
            # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
            top = stack.pop()
            visited.append(top)
            # 인접 노드를 방문한다.
            for adj in self.graph[top]:
                if adj not in visited:
                    stack.append(adj)

        return visited

if __name__ == "__main__":

    s = Solution()

    assert s.dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
    assert s.dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]