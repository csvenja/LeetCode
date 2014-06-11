# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        result = []
        current = root
        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.left = TreeNode(4)
p.right.left.right = TreeNode(5)

result = Solution()
print result.inorderTraversal(p)
