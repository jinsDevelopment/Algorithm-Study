from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        counter = Counter(stones)

        cnt = 0

        for char in jewels:
            if char in counter:
                cnt += counter.get(char)

        return cnt



if __name__ == "__main__":

    s =  Solution()

    jewels = "aA"
    stones = "aAAbbbb"
    print(s.numJewelsInStones(jewels, stones))


