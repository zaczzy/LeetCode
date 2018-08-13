class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            maxArea = max(maxArea, area)
            lowerHeight = min(height[i], height[j])
            while i < j and height[i] <= lowerHeight:
                i += 1
            while i < j and height[j] <= lowerHeight:
                j -= 1
        return maxArea