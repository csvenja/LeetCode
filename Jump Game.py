class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        far = 0
        for i in xrange(n):
            if i > far:
                break
            if i + A[i] > far:
                far = i + A[i]
            if far >= n - 1:
                return True
        return far >= n - 1

# A = [2, 3, 1, 1, 4]
A = [3, 2, 1, 0, 4]

result = Solution()
print result.canJump(A)
