from typing import List

class Solution:
    # 단지번호 붙이기
    def addressNumber(self, line: int, arrays: List) -> int:

        # arrays = [
        #     "0110100",
        #     "0110101",
        #     "1110101",
        #     "0000111",
        #     "0100000",
        #     "0111110",
        #     "0111000"
        # ]

        graph = []
        num = []

        self.count = 0
        result = 0


        graph = [[0 for col in range(line)] for row in range(line)]

        for idx, val in enumerate(arrays):
            for i in range(len(val)):
                graph[idx][i] = int(val[i])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def DFS(x, y):

            if x < 0 or x >= line or y < 0 or y >= line:
                return False
            print(x, y)
            if graph[x][y] == 1:
                self.count += 1
                graph[x][y] = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    DFS(nx, ny)
                return True
            return

        for i in range(line):
            for j in range(line):

                if DFS(i, j) == True:
                    num.append(self.count)
                    result += 1
                    self.count = 0
                    break

        return num



if __name__ == "__main__":
    s = Solution()

    rows = 7
    arrays =[
            "0110100",
            "0110101",
            "1110101",
            "0000111",
            "0100000",
            "0111110",
            "0111000"
            ]

    print(s.addressNumber(rows,arrays))