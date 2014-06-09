class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        profit = 0

        if n <= 1:
            return profit

        profit_forward = [0] * n
        min_forward = prices[0]

        for i in xrange(1, n):
            min_forward = min(min_forward, prices[i])
            profit_forward[i] = max(profit_forward[i - 1], prices[i] - min_forward)
            # buy at min_forward, sell at i

        profit_backward = [0] * n
        max_backward = prices[-1]

        for i in xrange(1, n):
            max_backward = max(max_backward, prices[n - i - 1])
            profit_backward[n - i - 1] = max(profit_backward[n - i], max_backward - prices[n - i - 1])
            profit = max(profit, profit_forward[n - i - 1] + profit_backward[n - i - 1])

        return profit

#a = []
#a = [2, 1]
a = [1, 2, 3, 4, 5, 8, 6, 7, 8, 9, 10]
a.reverse()

result = Solution()
print result.maxProfit(a)
