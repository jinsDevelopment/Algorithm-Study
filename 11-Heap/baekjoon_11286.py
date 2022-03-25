import heapq
import sys

class Solution:
    def absHeap(self):

        heap = list()
        for _ in range(int(sys.stdin.readline())):
            num = int(sys.stdin.readline().strip())

            if num == 0 and not heap:
                print(0)
            elif num == 0:
                print(heapq.heappop(heap)[1])
            else:
                # 여기서 (-value,value)로 구성된 튜플을 만들어서 heappush 함수의 인자로 주게 되면 튜플의 0번째 원소인 -value를 기준으로 heap을 구성하게 된다.
                # 기존의 value가 가장 클수록 -value의 값이 가장 작은 값이 되어 루트 노드에 올 수 있게 된다.
                heapq.heappush(heap, (num, num)) if num > 0 else heapq.heappush(heap, (-num, num))






if __name__ == "__main__":
    s = Solution()

    s.absHeap()