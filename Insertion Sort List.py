# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        pre_head = ListNode(0)
        new = pre_head
        current = head
        while current:
            new = pre_head
            while new.next and new.next.val < current.val:
                new = new.next
            tmp = current.next
            current.next = new.next
            new.next = current
            current = tmp
        return pre_head.next

a = ListNode(5)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e

result = Solution()
ans = result.insertionSortList(a)
while ans:
    print ans.val
    ans = ans.next
