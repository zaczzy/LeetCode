import math


class Solution(object):
    def reverse(self, x):
        """
        Reverses the integer if it does not overflow the 32 bit signed integer constraint,
        otherwise return 0
        :type x: int
        :rtype: int
        """
        # figure out how many digits there are
        if x >= math.pow(2, 32) or x < -math.pow(2, 31): return 0
        num_digits = 1
        while abs(x) // math.pow(10, num_digits) != 0:
            num_digits += 1
        x_str = str(x)
        x_rev = ''
        for i in range(1, num_digits + 1):
            x_rev = x_rev + x_str[-i]
        if x < 0: x_rev = '-' + x_rev
        return int(x_rev)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))
