from collections import deque

class Solution:

    def island_bfs(self,grid):
        # 0, 0
        nx = [1, -1, 0 ,0]
        ny = [0, 0, 1, -1]

        rows, cols = len(grid), len(grid[0])
        cnt = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue

                cnt += 1
                q = deque([(row, col)])

                while q:
                    x, y =q.popleft()
                    for i in range(4):
                        dx = x + nx[i]
                        dy = y + ny[i]
                        print(dx, dy)
                        if dx < 0 or dx >= rows or dy < 0 or dy >= cols or grid[dx][dy] != '1':
                            continue
                        grid[dx][dy] = '0'
                        q.append((dx,dy))
                        print(q)
        print(cnt)
        return cnt







if __name__ == "__main__":

    s = Solution()

    assert s.island_bfs(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1
    assert s.island_bfs(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
