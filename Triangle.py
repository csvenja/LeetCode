class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n < 1:
            return 0
        length = [triangle[n - 1][i] for i in xrange(n)]
        for i in xrange(n - 1):
            for j in xrange(n - i - 1):
                length[j] = min(length[j], length[j + 1]) + triangle[n - i - 2][j]
        return length[0]

# triangle = [[2],
#             [3, 4],
#             [6, 5, 7],
#             [4, 1, 8, 3]]

triangle = []

result = Solution()
print result.minimumTotal(triangle)
