class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0
        two = 0
        for i in xrange(len(A)):
            one = (one ^ A[i]) & ~two
            two = (two ^ A[i]) & ~one
        return one

A = [1, 1, 1, 2]

result = Solution()
print result.singleNumber(A)
