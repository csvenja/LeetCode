# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left is not None:
            root.left.next = root.right
        if root.right is not None:
            if root.next is None:
                root.right.next = None
            else:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

result = Solution()
result.connect(a)
left = a
current = a
while current is not None:
    print current.val
    current = current.next
    if current is None:
        left = left.left
        current = left
        print
