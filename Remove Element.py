class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n = len(A)
        for i in xrange(n):
            if A[n - i - 1] == elem:
                del A[n - i - 1]
        return len(A)

A = [1, 2, 3, 5, 1, 2, 1, 3]
elem = 1

result = Solution()
print result.removeElement(A, elem)
