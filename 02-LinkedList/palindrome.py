def isPalindrome(head):
    arr = []

    if not head:
        return True

    node = head
    cnt = 0
    while node:
        cnt = cnt + 1
        print(cnt, " :: ",node.val)
        arr.append(node.val)
        node = node.next

    while len(arr) > 1:
        if arr.pop(0) != arr.pop(): #arr.pop()는 맨 마지막 인덱스 제거
            return False

    return True