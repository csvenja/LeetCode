class Solution:
    # @return an integer
    def romanToInt(self, s):
        num = 0
        s = s[::-1]
        for i in s:
            if i == 'I':
                num += 1 if num < 5 else -1
            elif i == 'V':
                num += 5
            elif i == 'X':
                num += 10 * (1 if num < 50 else -1)
            elif i == 'L':
                num += 50
            elif i == 'C':
                num += 100 * (1 if num < 500 else -1)
            elif i == 'D':
                num += 500
            elif i == 'M':
                num += 1000
            else:
                pass
        return num

s = 'X'

result = Solution()
print result.romanToInt(s)
