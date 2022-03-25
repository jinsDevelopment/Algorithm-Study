from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()

        for n in nums:
            heapq.heappush(heap,-n)

        for _ in range(1,k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # 최소 힙 구조
        print(nums)

        for i in range(len(nums)- k):   # 6 - 2
            heapq.heappop(nums)
            print(i, nums)


        return heapq.heappop(nums)


if __name__ == "__main__":
    s = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(s.findKthLargest(nums, k))
    # print(s.findKthLargest2(nums, k))