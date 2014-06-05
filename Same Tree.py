# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None or p is not None and q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

p = TreeNode(1)
p.left = TreeNode(2)
p.left.right = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(2)
q.left.right = TreeNode(3)

result = Solution()
print result.isSameTree(p, q)
