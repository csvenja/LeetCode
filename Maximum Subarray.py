class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSum = -9999999
        curSum = 0
        for i in xrange(len(A)):
            curSum += A[i]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum
    # maxSum = -999999

    # def maxSubArray(self, A):
    #     n = len(A)
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return A[0]
    #     maxSum = -999999
    #     self.maxSubArrayRecursion(A, 0, n - 1)
    #     return maxSum

    # def maxSubArrayRecursion(self, A, left, right):
    #     if left == right:
    #         return A[left]
    #     mid = (left + right) / 2
    #     left_sub = self.maxSubArrayRecursion(A, left, mid)
    #     right_sub = self.maxSubArrayRecursion(A, mid + 1, right)
    #     left_max = A[mid]
    #     right_max = A[mid + 1]
    #     tmp = 0
    #     for i in reversed(A[left:mid + 1]):
    #         tmp += i
    #         left_max = max(left_max, tmp)
    #     print A[left:mid + 1]
    #     tmp = 0
    #     for i in A[mid + 1:right + 1]:
    #         tmp += i
    #         right_max = max(right_max, tmp)
    #     return max(max(left_sub, right_sub), left_max + right_max)

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# A = [-2, 3, -2, 4]

result = Solution()
print result.maxSubArray(A)
