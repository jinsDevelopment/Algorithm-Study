import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums).most_common(k)
        ans : List[int] = []

        for i in range(len(freqs)):
            ans.append(freqs[i][0])

        return ans




if __name__ == "__main__":

    s =  Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    print(s.topKFrequent(nums, k))