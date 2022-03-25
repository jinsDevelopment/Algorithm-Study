from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        prev_element = []

        def dfs(element):
            if len(nums) == len(prev_element):
                result.append(prev_element[:])

            for e in element:
                next_element = element[:]
                next_element.remove(e)

                prev_element.append(e)
                dfs(next_element)
                prev_element.pop()

        dfs(nums)
        return result

    def permutation(self, arr, r):
        arr = sorted(arr)
        used = [0 for _ in range(len(arr))]
        return_array = []
        def generate(chosen, used):
            # 내가 원하는 만큼 뽑았으면, return
            if len(chosen) == r:
                return_array.append(chosen[:])
                return

            for i in range(len(arr)):
                if not used[i]:
                    chosen.append(arr[i])
                    used[i] = 1
                    generate(chosen, used)
                    used[i] = 0
                    chosen.pop()

        generate([], used)
        return return_array

    def dfs_perm_stack(self, lst, n):
        ret = []
        idx = [i for i in range(len(lst))]

        stack = []
        for i in idx:
            stack.append([i])

        while len(stack) != 0:
            cur = stack.pop(0)

            for i in idx:
                if i not in cur:
                    temp = cur + [i]
                    if len(temp) == n:
                        element = []
                        for i in temp:
                            element.append(lst[i])
                        ret.append(element)
                    else:
                        stack.append(temp)
        return ret



    def permutePythonBook(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))



if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3]


    print(s.permute(nums))
    print(s.permutation(nums,3))
    print(s.dfs_perm_stack(nums,3))
    print(s.permutePythonBook(nums))