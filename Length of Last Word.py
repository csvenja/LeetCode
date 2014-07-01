class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split()
        if len(words) < 1:
            return 0
        return len(words[-1])

s = "Hello World"
s = ""

result = Solution()
print result.lengthOfLastWord(s)
