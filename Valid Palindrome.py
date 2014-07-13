class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

s = 'A man, a plan, a canal: Panama'
s = 'race a car'
s = '1a2'
s = ' '

result = Solution()
print result.isPalindrome(s)
