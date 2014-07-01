class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num = int(''.join([str(i) for i in digits]))
        num += 1
        num = str(num)
        return [int(i) for i in num]

digits = [1, 2, 3, 4, 5]

result = Solution()
print result.plusOne(digits)
