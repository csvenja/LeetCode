class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n = len(num)
        d = {}
        for i in xrange(n):
            if num[i] in d:
                return (d[num[i]] + 1, i + 1)
            else:
                d[target - num[i]] = i

num = [2, 7, 11, 15]
target = 9

result = Solution()
print result.twoSum(num, target)
