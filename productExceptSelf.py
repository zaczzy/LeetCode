class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftAccumulateProduct = [1 for _ in range(len(nums))]
        leftAccumulateProduct[0] = nums[0]
        for i in range(1, len(nums)):
            leftAccumulateProduct[i] = leftAccumulateProduct[i - 1] * nums[i]

        rightAccumulateProduct = [1 for _ in range(len(nums))]
        rightAccumulateProduct[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            rightAccumulateProduct[i] = rightAccumulateProduct[i + 1] * nums[i]

        ans = nums
        for i in range(len(nums)):
            if i == 0:
                ans[i] = 1 * rightAccumulateProduct[i + 1]
            elif i == len(nums) - 1:
                ans[i] = 1 * leftAccumulateProduct[i - 1]
            else:
                ans[i] = leftAccumulateProduct[i - 1] * rightAccumulateProduct[i + 1]
        return ans