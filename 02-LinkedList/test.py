from palindrome import isPalindrome
from structures import LinkedList

l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)

print(isPalindrome(l1.head))
print(isPalindrome(l2.head))

# assert isPalindrome(l1.head)
# assert not isPalindrome(l2.head)


