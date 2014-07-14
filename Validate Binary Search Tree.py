# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    pre = -999999

    def isValidBST(self, root):
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

p1 = TreeNode(10)
p2 = TreeNode(5)
p3 = TreeNode(15)
p4 = TreeNode(6)
p5 = TreeNode(20)
p1 = TreeNode(1)
p2 = TreeNode(0)
p3 = TreeNode(3)
p4 = TreeNode(2)
p5 = TreeNode(5)
p1.left = p2
p1.right = p3
p3.left = p4
p3.right = p5

result = Solution()
print result.isValidBST(p1)
