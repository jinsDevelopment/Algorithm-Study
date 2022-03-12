from typing import Optional
from structures import ListNode, LinkedList

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prv = head, None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        return prv


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result = solution.reverseList(head)

    while result:
        print(result.val)
        result = result.next




