class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        index_map = {}
        for inx, itm in enumerate(nums):
            if itm not in index_map:
                index_map[itm] = inx
            elif itm == target / 2:
                return sorted([inx, index_map[itm]])
            else:
                index_map.pop(itm)
        nums = set(nums)
        for itm in nums:
            if target - itm in nums:
                nums.remove(itm)
                if target - itm in nums:
                    return sorted([index_map[itm], index_map[target - itm]])