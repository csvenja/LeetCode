class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

#a = []
a = [2, 1]
#a = [1, 2, 3, 4, 5, 7, 6, 7, 8, 9, 10]
#a.reverse()

result = Solution()
print result.maxProfit(a)
