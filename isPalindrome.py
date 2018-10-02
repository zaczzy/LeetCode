class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return "".join(list(reversed(list(str(x))))) == str(x)