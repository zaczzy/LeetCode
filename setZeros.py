class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowsToClean = set()
        colsToClean = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToClean.add(i)
                    colsToClean.add(j)

        for row in rowsToClean:
            matrix[row] = [0 for _ in range(len(matrix[0]))]
        for col in colsToClean:
            for inx in range(len(matrix)):
                matrix[inx][col] = 0
    # better solution: everytime a zero is encountered, push the 0 to its row head and column head,
    # then delete the corresponding rows and columns

if __name__ == "__main__":
    matrix = [[1], [0]]
    Solution().setZeroes(matrix)
    print(matrix)