# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        traversal = []
        current = [root]
        next = []
        while len(current) > 0:
            values = []
            for item in current:
                values.append(item.val)
                if item.left:
                    next.append(item.left)
                if item.right:
                    next.append(item.right)
            traversal.insert(0, values)
            current = next
            next = []
        return traversal

p1 = TreeNode(3)
# p2 = TreeNode(9)
# p3 = TreeNode(20)
# p4 = TreeNode(15)
# p5 = TreeNode(7)
# p1.left = p2
# p1.right = p3
# p3.left = p4
# p3.right = p5
# p1 = None

result = Solution()
print result.levelOrderBottom(p1)
