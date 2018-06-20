class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        sum = 0;
        for i,x in enumerate(s):
            sum += (ord(x) - 64) * (26**i)
        return sum