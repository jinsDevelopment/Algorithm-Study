from typing import List

class Solution:
    # 책 풀이1
    def arrayPairSum_book1(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    # 책 풀이2
    def arrayPairSum_book2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n

        return sum

    # 책 풀이3
    def arrayPairSum_book3(self, nums):
        nums = sorted(nums)
        return sum(nums[::2])

if __name__ == "__main__":
    solution = Solution()
    nums =  [1,4,3,2]
    print(solution.arrayPairSum_book1(nums))
    print(solution.arrayPairSum_book2(nums))
    nums = [6, 2, 6, 5, 1, 2]
    print(solution.arrayPairSum_book1(nums))
    print(solution.arrayPairSum_book2(nums))

