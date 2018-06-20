class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alphabet_list = [chr(c) for c in range(ord('A'),ord('Z') + 1)]  # create a list from A-Z
        result = ""
        while n > 0:
            result += alphabet_list[(n-1)%26]     # Assigns the alphabets from start to end
            n = (n - 1) // 26
        return result[::-1]   # reverse it for desired result
