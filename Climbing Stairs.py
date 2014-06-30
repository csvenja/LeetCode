class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        step = [0 for i in xrange(n + 1)]
        step[1] = 1
        step[2] = 2
        for i in xrange(3, n + 1):
            step[i] = step[i - 1] + step[i - 2]
        return step[n]

result = Solution()
print result.climbStairs(1)
