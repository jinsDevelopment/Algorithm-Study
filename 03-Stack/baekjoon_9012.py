class Solution:
    def is_valid_parenthesis(self,s):

        stack = []

        for bracket in s:
            # print(bracket)
            if not stack and bracket == "(":
                stack.append(bracket)
                continue
            elif not stack and bracket == ")":
                return "NO"

            if stack and bracket == "(":
                stack.append(bracket)
            elif stack and bracket == ")":
                stack.pop()

        if stack:
            return "NO"

        return "YES"



if __name__ == "__main__":
    s = Solution()
    print(s.is_valid_parenthesis("(())())"))
    print(s.is_valid_parenthesis("(((()())()"))
    print(s.is_valid_parenthesis("(()())((()))"))
    print(s.is_valid_parenthesis("((()()(()))(((())))()"))
    print(s.is_valid_parenthesis("()()()()(()()())()"))
    print(s.is_valid_parenthesis("(()((())()("))

    print(s.is_valid_parenthesis("(("))
    print(s.is_valid_parenthesis("))"))
    print(s.is_valid_parenthesis("())(()"))

    print(s.is_valid_parenthesis("())("))

