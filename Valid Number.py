class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            a = float(s)
            return True
        except:
            return False
