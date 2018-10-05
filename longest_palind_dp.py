# Filling a triangular DP table of booleans, our last to fill is t[0, n-1], first to fill is t[k, k] = true.
# then we keep track of maximum value pair of all i, j to maximize j - i such that  t[i, j] = true.


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1: return s
        indexMatrix = [[False for _ in range(len(s))] for _ in range(len(s))]
        maxLength = 0
        maxPosition = (0, 0)
        for i in range(len(s)):
            indexMatrix[i][i] = True

        for i in range(len(s) - 1):
            startPosition = (0, i + 1)
            for j in range(len(s) - 1 - i):
                position = (startPosition[0]+j, startPosition[1]+j)
                if position[1] - 1 < position[0] + 1:
                    indexMatrix[position[0]][position[1]] = s[position[0]] == s[position[1]]
                else:
                    indexMatrix[position[0]][position[1]] = s[position[0]] == s[position[1]] \
                                                            and indexMatrix[position[0] + 1][position[1] - 1]
                if indexMatrix[position[0]][position[1]] and position[1] - position[0] > maxLength:
                    maxPosition = (position[0], position[1])
                    maxLength = position[1] - position[0]

        return s[maxPosition[0]: maxPosition[1] + 1]


# After reading the faster solution, the trick is that we consider each character to be the center of some palindromic
# substring, and test the nearby characters around that center to see how long that palindromic substring is, then
# return the maximum. Simple idea, faster execution. This is a dynamic programming exercise.

