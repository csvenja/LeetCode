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
    def connect_recursion(self, root):
        if root is None:
            return
        first = root.next
        while first is not None:
            if first.left is not None:
                first = first.left
                break
            if first.right is not None:
                first = first.right
                break
            first = first.next
        if root.right is not None:
            root.right.next = first
        if root.left is not None:
            root.left.next = first
            if root.right is not None:
                root.left.next = root.right
        self.connect(root.right)  # right to left to find next
        self.connect(root.left)

    def connect_loop(self, root):
        upperLevelHead = root
        currentLevelHead = None
        currentPreNode = None
        while upperLevelHead:
            current = upperLevelHead
            while current:
                if current.left:
                    if currentLevelHead:
                        currentPreNode.next = current.left
                        currentPreNode = currentPreNode.next
                    else:
                        currentLevelHead = current.left
                        currentPreNode = currentLevelHead
                if current.right:
                    if currentLevelHead:
                        currentPreNode.next = current.right
                        currentPreNode = currentPreNode.next
                    else:
                        currentLevelHead = current.right
                        currentPreNode = currentLevelHead
                current = current.next
            upperLevelHead = currentLevelHead
            currentLevelHead = None

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.right = TreeNode(7)

result = Solution()
result.connect_recursion(a)
result.connect_loop(a)
left = a
current = a
while current is not None:
    print current.val
    current = current.next
    if current is None:
        left = left.left
        current = left
        print
