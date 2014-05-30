class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target > A[-1]:
            return len(A)
        for i in xrange(len(A) - 1):
            if A[i] < target and A[i + 1] >= target:
                return i + 1
        return 0

A = [1, 3, 5, 6]
target = 5

result = Solution()
print result.searchInsert(A, target)
