from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        스택으로 할 거면 스택의 연산을 제대로 활용해야 함
        -> 대신 이때는 이미 넣었던 애를 pop해야 하는 거라 조건 설정이 조금 까다로움
        -> 이미 들어간 애를 확인해야 하므로 스택만으로는 안되고 다른 객체를 하나 더 만들어서 확인해야 함.
        -> 몇 번이나 등장하는지를 확인해야하므로 collections.Counter를 활용할 것임 (이 부분을 처음 접근할 때 생각을 못했음.)
        """

        counter, stack, seen = Counter(s), [], set()

        for char in s:
            counter[char] -= 1  # 한 글자가 탐색되었다고 명시해줌.
            if char in seen:  # 이미 문자열에 추가되었다면
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                # while stack -> stack이 비어있으면, 즉 처음 시점
                # 왜 while? "bcabc" 같은 경우, b와 c는 그대로 stack에 push되고 a를 만나면 둘 다 pop되어야 함.
                # while이 아니면 c만 pop되고 b는 pop이 안되므로
                seen.remove(stack.pop())  # stack에서 pop하고, 해당 글자를 seen에서 지움
            stack.append(char)
            seen.add(char)

        return "".join(stack)

    def removeDuplicateLetters_book1(self, s: str) -> str:
        # 집합으로 정렬

        print(sorted((set(s))))

        for char in sorted(set(s)):
            print(char)
            print(s[s.index(char):])
            suffix = s[s.index(char):]

            print(set(suffix))
            # 전체 집합과 접미사 집합이 일치할때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


    def removeDuplicateLetters_book2(self, s: str) -> str:

        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()

    print(s.removeDuplicateLetters_book1("bcabc"))
    print(s.removeDuplicateLetters_book1("cbacdcbc"))