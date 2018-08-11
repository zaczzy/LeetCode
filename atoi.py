# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
# digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed
# integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values,
# INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
# Test results: after fixing functional mistakes we missed these inputs: "-", "+1"


class Solution:
    def myAtoi(self, input):
        """
        :type input: str
        :rtype: int
        """
        if input.startswith(' ') or input.endswith(' '):
            input = input.strip()
        if len(input) == 0:
            return 0
        if input[0] not in "123456789" and input[0] != "-":
            return 0

        if input[0] == "-":
            numeral = "-"
            input = input[1:]
        else:
            numeral = ""

        inx = 0
        while inx < len(input) and input[inx] in "0123456789":
            numeral = numeral + input[inx]
            inx += 1

        if numeral == "-" or numeral == "":
            return 0

        numeral = int(numeral)
        if numeral < -pow(2, 31):
            return -pow(2, 31)
        elif numeral > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return numeral
