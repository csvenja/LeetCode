# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        head = TreeNode(0)
        result = head
        while len(stack) > 0:
            current = stack.pop()
            result.right = current
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
            result.left = None
            result = result.right
        return head.right

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(5)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right.right = TreeNode(6)

# p = TreeNode(1)
# p.right = TreeNode(2)
# p.right.left = TreeNode(3)

result = Solution()
ans = result.preorderTraversal(p)
while ans:
    print ans.val
    ans = ans.right
