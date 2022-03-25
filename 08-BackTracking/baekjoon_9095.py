class Solution:
    def oneTwoThreeSum(self, n: int) -> int:

        cnt = 0

        def dfs(num,sum):
            nonlocal cnt
            if sum == num:
                cnt += 1
                return

            elif sum > num:
                return

            for i in range(1,4):
                sum += i
                dfs(num, sum)
                sum -= i

        dfs(n,0)


        return cnt



if __name__ == "__main__":
    s = Solution()

    print(s.oneTwoThreeSum(4))