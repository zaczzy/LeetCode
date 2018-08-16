class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for i in range(len(nums)):
            newAns = []
            for set in ans:
                newAns.append(set.copy())
                set.append(nums[i])
                newAns.append(set.copy())
            ans = newAns
        return ans

