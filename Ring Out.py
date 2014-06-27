class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


class Solution:
    def ringOut(self, n):
        head = ListNode(1)
        current = head
        for i in xrange(2, n + 1):
            item = ListNode(i)
            item.prev = current
            current.next = item
            current = current.next
        head.prev = current
        current.next = head
        current = head
        count = n
        while count > 1:
            current.prev.next = current.next
            current.next.prev = current.prev
            current = current.next.next
            count = count - 1
        return current.val

result = Solution()
print result.ringOut(100000)
