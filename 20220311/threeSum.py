from collections import Counter
from typing import List

class Solution(object):
    # 혼자 풀이(런타임 에러)
    def threeSum(self, nums):

        answer = []
        # 3개의 값의 합이므로 len(nums) < 3이면 빈 값 return
        if len(nums) < 3:
            return answer
        if max(nums) == 0:
            answer.append([0,0,0])
            return answer

        # nums 배열 오름차순 정렬
        nums = sorted(nums)

        # len(nums) 만큼 for문 수행
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        array = []
                        array.append(nums[i])
                        array.append(nums[j])
                        array.append(nums[k])
                        answer.append(array)

        if len(answer) == 1:
            return answer

        answer = sorted(answer)
        an = []
        print(answer)
        for ans in range(len(answer)):

            dic = Counter(answer[ans])
            if dic != Counter(answer[ans+1]):
                an.append(answer[ans])
            else:
                if ans+1 == len(answer)-1:
                    an.append(answer[ans])
                    break;
        return an

    # 책 풀이
    def threeSum_book(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # `sum = 0`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))
    nums = [0, 0, 0]
    print(solution.threeSum(nums))
    nums = [1,1,-2]
    print(solution.threeSum(nums))
    nums = [-2,0,0,2,2]
    print(solution.threeSum(nums))
    nums = [-1, 0, 1]
    print(solution.threeSum(nums))
    nums = [0, 0, -1]
    print(solution.threeSum(nums))
    nums = [-2,0,1,1,2]
    print(solution.threeSum(nums))