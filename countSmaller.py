import bisect
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        inOrder = [nums[len(nums) - 1]]

        for i in range(len(nums) - 2, -1 , -1):
            inOrder = bisect.insort_left(inOrder, nums[i], 0, len(inOrder) - 1)
            # Yet to finish: from right to left, maintain a sorted increasing list, every time we binary search and
            # insert the value while returning the number of elements on the left of it in sorted order list
