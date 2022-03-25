from collections import Counter

class Solution:
    # 혼자 풀이(성공) + 구글링
    def longestPalindrome(self, str):

        dic = Counter(str)
        count = 0
        max = 0

        print(dic)
        if len(dic) == 1:
            return len(str)

        for val in dic.values():
            if val % 2 == 1:
                count = count + val - 1
                if max == 0:
                    max = 1
            else:
                count = count + val
        return count + max


    # 책 풀이
    def longestPalindrome_book(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result




if __name__ == "__main__":
    solution = Solution()
    strs = "abccccdd"
    print(solution.longestPalindrome(strs))
    strs = "a"
    print(solution.longestPalindrome(strs))
    strs = "bb"
    print(solution.longestPalindrome(strs))
    strs = "ccc"
    print(solution.longestPalindrome(strs))
    strs = "bananas"
    print(solution.longestPalindrome(strs))