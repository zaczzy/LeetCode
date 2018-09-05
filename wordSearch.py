from collections import defaultdict


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def getId(i, j):
            return i * len(board[0]) + j

        def withinBound(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        letterToID = defaultdict(list)
        adjList = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                letterToID[board[i][j]].append(getId(i, j))
                if withinBound(i - 1, j):
                    adjList[getId(i, j)].append(getId(i - 1, j))
                if withinBound(i + 1, j):
                    adjList[getId(i, j)].append(getId(i + 1, j))
                if withinBound(i, j - 1):
                    adjList[getId(i, j)].append(getId(i, j - 1))
                if withinBound(i, j + 1):
                    adjList[getId(i, j)].append(getId(i, j + 1))

        def dfs_visit(id, nextLetter):
            neighborSet = set(adjList[id])
            letterSet = set(letterToID[nextLetter])
            targetIds = neighborSet.intersection(letterSet)
            for targetId in targetIds:
                dfs_visit()