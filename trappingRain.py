class Solution:
    def trim(self, peaks):
        needTrim = True
        while needTrim:
            peaks = dict(enumerate(peaks.values()))
            counter = [0 for _ in range(len(peaks))]
            for i in range(len(peaks) - 1):
                if peaks[i][1] > peaks[i + 1][1]:
                    counter[i + 1] += 1
                elif peaks[i][1] < peaks[i + 1][1]:
                    counter[i] += 1
                else:
                    counter[i] += 1
                    counter[i + 1] += 1
            needTrim = False
            for j in range(len(counter)):
                if counter[j] > 1:
                    needTrim = True
                    peaks.pop(j)
        return list(peaks.values())

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        volTrap = 0
        localMaximum = []
        if height[0] >= height[1]:
            localMaximum.append((0, height[0]))
        last = len(height) - 1
        for i in range(1, last, 1):
            if height[i] >= height[i - 1] and height[i] >= height[i + 1]:
                localMaximum.append((i, height[i]))
        if height[last] >= height[last - 1]:
            localMaximum.append((last, height[last]))
        print(localMaximum)
        localMaximum = self.trim(dict(enumerate(localMaximum)))
        for peakInx in range(len(localMaximum) - 1):
            boundaryHeight = min(localMaximum[peakInx][1], localMaximum[peakInx + 1][1])
            volEmpty = (localMaximum[peakInx + 1][0] - localMaximum[peakInx][0] - 1) \
                       * boundaryHeight
            volSolid = 0
            for j in range(localMaximum[peakInx][0] + 1, localMaximum[peakInx + 1][0], 1):
                volSolid += min(height[j], boundaryHeight)
            volReal = volEmpty - volSolid
            volTrap += volReal
        return volTrap


if __name__ == "__main__":
    print(Solution().trap([5, 2, 1, 2, 1, 5]))
    # print(Solution().trim([(0, 5), (3, 2), (5, 5)]))
