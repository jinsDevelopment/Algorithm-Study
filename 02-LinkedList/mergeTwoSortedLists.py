from typing import Optional
from structures import ListNode

class Solution:
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        cur = ListNode()
        head = cur

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.next = list1
                cur, list1 = list1, list1.next
            else:
                cur.next = list2
                cur, list2 = list2, list2.next

        if list1 != None:
            cur.next = list1
        else:
            cur.next = list2

        return head.next

if __name__ == "__main__":
    solution = Solution()

    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    result = solution.mergeTwoLists(node1, node2)

    while (result):
        print(result.val)
        result = result.next