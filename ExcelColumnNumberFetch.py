class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]     #inverting the string
        sum = 0;
        for i,x in enumerate(s):
            sum += (ord(x) - 64) * (26**i)      #fetching the numeric value and multiplying it with base 26**index
        return sum
