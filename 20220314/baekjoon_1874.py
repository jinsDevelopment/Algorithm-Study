class Solution:
    def stack_sequence(self,nums):

        temp = True
        stack = []
        answer = []
        count = 1

        for num in nums:

            while count <= num:  # 입력된 수열보다 작은 경우 같아질 때까지 반복
                stack.append(count)
                answer.append('+')
                count += 1
            if stack[-1] == num:  # 입력된 수열과 동일한 경우
                stack.pop()
                answer.append('-')
            else:  # 특정 수열을 만들 수 없을 경우
                temp = False

        if not temp:
            return 'NO'
        else:
            li = []
            for i in answer:
                li.append(i)
            return '    '.join(li)

if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 6, 8, 7, 5, 2, 1]

    print(s.stack_sequence(nums))

    nums = [1 ,2 ,5 ,3 ,4]
    print(s.stack_sequence(nums))

