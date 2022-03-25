import heapq
import sys

class Solution:
    def minHeap(self):

        heap = list()
        for _ in range(int(sys.stdin.readline())):
            num = int(sys.stdin.readline().strip())


            if num == 0 and not heap:
                print(0)
            elif num == 0:
                print(heapq.heappop(heap))
            else:
                heapq.heappush(heap, num)





if __name__ == "__main__":
    s = Solution()

    s.minHeap()