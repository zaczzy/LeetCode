class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = []
        for _ in range(numRows):
            rows.append([])
        loop = 2 * numRows - 2
        for outer in range(len(s) // loop + 1):
            for inner in range(loop):
                print(outer, inner)
                rows[numRows - 1 - abs(inner - numRows + 1)].append(s[outer * loop + inner])
        result = ""
        for row_num in range(len(rows)):
            result = result + ''.join(rows[row_num])
        return result


if __name__ == "__main__":
    test_str = "PAYPALISHIRING"
    print(Solution().convert(test_str, 3))
#  the problem now is that the last loop is incomplete