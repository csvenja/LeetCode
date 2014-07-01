# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        current = head
        array = []
        while current:
            array.append(current)
            current = current.next
        n = len(array)
        return self.generateBST(n, array)

    def generateBST(self, n, array):
        if n == 0:
            return None
        if n == 1:
            return TreeNode(array[0].val)
        flag = n / 2
        root = TreeNode(array[flag].val)
        root.left = self.generateBST(n / 2, array[0:n / 2])
        root.right = self.generateBST(len(array[n / 2 + 1:n]), array[n / 2 + 1:n])
        return root


def preorderTraversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)
p7 = ListNode(7)
p8 = ListNode(8)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8

result = Solution()
ans = preorderTraversal(result.sortedListToBST(p1))
print ans
