class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        profit = 0
        min_before = prices[0]
        for i in xrange(n):
            min_before = min(min_before, prices[i])
            profit = max(profit, prices[i] - min_before)
        return profit

#a = []
#a = [2, 1]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a.reverse()

result = Solution()
print result.maxProfit(a)
