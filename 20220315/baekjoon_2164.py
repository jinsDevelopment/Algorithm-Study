import collections

class Solution:
    def cardQueue(self,N):

        deque = collections.deque()

        for i in range(1, N + 1):
            deque.append(i)

        while len(deque) > 1:
            deque.popleft()
            move_num = deque.popleft()
            deque.append(move_num)

        return deque[0]








if __name__ == "__main__":
    s = Solution()

    print(s.cardQueue(6))


