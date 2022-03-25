from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]]

        for num in nums:
            size = len(result)
            for y in range(size):
                result.append(result[y] + [num])
                # print(result)

        return result

    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:

        result = []

        def dfs(index, path):
            # print(path)
            #매번 결과 추가
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0,[])

        return result







if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]

    print(s.subsets(nums))
    print(s.subsets_dfs(nums))