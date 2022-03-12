from typing import Optional
from structures import ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        odd = head
        even = head.next
        evenhead = even

        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = evenhead
        return head


if __name__ == "__main__":
    solution = Solution()

    l1_node4 = ListNode(5,None)
    l1_node3 = ListNode(4, l1_node4)
    l1_node2 = ListNode(3, l1_node3)
    l1_node1 = ListNode(2, l1_node2)
    l1_head1 = ListNode(1, l1_node1)

    result = solution.oddEvenList(l1_head1)

    while result:
        print(result.val)
        result = result.next