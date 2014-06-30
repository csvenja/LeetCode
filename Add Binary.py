class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_int = int(a, 2)
        b_int = int(b, 2)
        c_int = a_int + b_int
        c = "{0:b}".format(c_int)
        return c

a = "11"
b = "1"

result = Solution()
print result.addBinary(a, b)
