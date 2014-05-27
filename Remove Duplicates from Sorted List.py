# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        pre = head
        current = head.next
        pre.next = None
        num = head.val
        while current:
            next = current.next
            current.next = None
            if current.val > num:
                num = current.val
                pre.next = current
                pre = pre.next
            current = next
        return head

p1 = ListNode(1)
p2 = ListNode(1)
p3 = ListNode(2)
p4 = ListNode(3)
p5 = ListNode(3)
p1.next = p3
# p2.next = p3
# p3.next = p4
# p4.next = p5

result = Solution()
ans = result.deleteDuplicates(p1)
while ans:
    print ans.val
    ans = ans.next
