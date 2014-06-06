class Solution:
    # @return an integer
    def reverse(self, x):
        x_string = str(x)
        sign = 1
        if x_string[0] == '-':
            sign = -1
            x_string = x_string[1:]
        x_string = x_string[::-1].strip('0')
        if len(x_string) == 0:
            x_string = '0'
        return sign * int(x_string)

result = Solution()
print result.reverse(-123000)