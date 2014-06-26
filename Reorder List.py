# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None:
            return
        array = []
        current = head
        while current:
            array.append(current)
            current = current.next
        n = len(array)
        flag = n / 2
        for i in xrange(flag):
            array[i].next = array[n - i - 1]
            array[n - i - 1].next = array[i + 1]
        array[flag].next = None
        return

# p1 = ListNode(1)
# p2 = ListNode(2)
# p3 = ListNode(3)
# p4 = ListNode(4)
# p5 = ListNode(5)
# p6 = ListNode(6)
# p1.next = p2
# p2.next = p3
# p3.next = p4
# p4.next = p5
# p5.next = p6

# p1 = None

p1 = ListNode(1)

result = Solution()
result.reorderList(p1)

while p1:
    print p1.val
    p1 = p1.next
