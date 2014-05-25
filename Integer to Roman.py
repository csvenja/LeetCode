class Solution:
    # @return a string
    int_dict = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_dict = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    def intToRoman(self, num):
        for i in xrange(len(self.int_dict)):
            if self.int_dict[i] <= num:
                return self.roman_dict[i] + self.intToRoman(num - self.int_dict[i])
        return ''

num = 2014

result = Solution()
print result.intToRoman(num)
