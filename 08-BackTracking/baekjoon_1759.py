from typing import List
import sys
import itertools

class Solution:
    def makePassword(self, L: int, C:int, arr:List[str]) -> int:

        # L, C = map(int, input().split())
        # arr = list(input().split())

        arr.sort()
        vowels = ['a', 'e', 'i', 'o', 'u']
        visited = [False for i in range(C)]

        temp = []
        # cnt는 현재 단어 length, start는 range 시작 위치
        def dfs(cnt, start):
            if cnt == L:
                v, c = 0, 0
                for i in temp:
                    if i in vowels:
                        v += 1
                    else:
                        c += 1
                if v >= 1 and c >= 2:
                    for i in temp:
                        print(i, end='')
                    print()
                return

            for i in range(start, C):
                if not visited[i]:
                    visited[i] = True
                    temp.append(arr[i])
                    dfs(cnt + 1, i + 1)
                    temp.pop()
                    visited[i] = False

        dfs(0, 0)

    def makePassword2(self) -> int:

        """
        l = 가능성있는 암호 길이 c = 전체 길이
        c개의 알파벳
        * 최소 한개의 모음과 최소 두 개의 자음
        * 모음(a,e,i,o,u)
        암호는 무조건 사전식으로! (abc= 가능, bac= 불가능)

        """

        input = sys.stdin.readline

        l, c = map(int, input().split())
        # input 값을 사전식으로 정렬
        wordList = sorted(list(input().split()))
        # l개의 경우를 모두 뽑아주고 특정 조건(모음 1개이상, 자음 2개 이상)을 만족하는 값만 보여주면 된다.
        vowel = ["a", "e", "i", "o", "u"]

        for _ in wordList:
            result = list(itertools.combinations(wordList, l))

        print(result)

        answer = []
        for res in result:
            v_count = 0
            c_count = 0

            for c in res:
                if c in vowel:
                    v_count += 1
                else:
                    c_count += 1

            if v_count > 0 and c_count > 1:
                answer.append(res)

        print("\n".join(["".join(s) for s in answer]), end="")





if __name__ == "__main__":
    s = Solution()

    n = 4
    m = 6
    array =["a", "t", "c", "i", "s", "w"]

    s.makePassword(n,m,array)

    # s.makePassword2()
