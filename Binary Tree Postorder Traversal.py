# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack = []
        result = []
        current = root
        previous = None
        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack[-1]
            if current.right is None or current.right is previous:
                result.append(current.val)
                stack.pop()
                previous = current
                current = None
            else:
                current = current.right
        return result

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.left = TreeNode(4)
p.right.left.right = TreeNode(5)

result = Solution()
print result.postorderTraversal(p)
