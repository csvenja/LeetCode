class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        sentence = s.split()
        sentence.reverse()
        s = " ".join(sentence)
        return s

s = "the sky is blue"

result = Solution()
print result.reverseWords(s)
