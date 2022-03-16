from sys import stdin

class Solution:
    def findNum(self,n, N, m, M):   #수 찾기

        N = set(N)
        ans = []
        for num in M:
            if num in N:
                ans.append(1)
            else:
                ans.append(0)
        return ans


if __name__ == "__main__":
    s = Solution()

    n = stdin.readline()
    N = stdin.readline().split()
    m = stdin.readline()
    M = stdin.readline().split()
    # 5
    # 4 1 5 2 3
    # 5
    # 1 3 7 9 5

    s.findNum(n,N,m,M)



