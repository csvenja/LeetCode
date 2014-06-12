# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        fast = head
        slow = head
        encounter = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                encounter = fast
                break
        if encounter is None:
            return None
        else:
            while head is not encounter:
                head = head.next
                encounter = encounter.next
            return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next

result = Solution()
print result.detectCycle(head)
