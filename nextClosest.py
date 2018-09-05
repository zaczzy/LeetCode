import bisect as b


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        num1 = int(time[0])
        num2 = int(time[1])
        num3 = int(time[3])
        num4 = int(time[4])
        nums = sorted([num1, num2, num3, num4])
        # case 1
        if num4 != nums[3]:
            inxNum4 = b.bisect(nums, num4, 0, 3)
            return time[:-1] + str(nums[inxNum4])
        # case 2
        elif num3 != nums[3]:
            inxNums3 = b.bisect(nums, num3, 0, 3)
            replace = nums[inxNums3]
            if replace < 6:
                return time[:-2] + str(replace) + str(nums[0])
            else:
                if self.detectCase3(nums, num1, num2, num3, num4):
                    return self.handleCase3(nums, num1, num2, num3, num4)
                else:
                    return self.handleCase4(nums)

        elif self.detectCase3(nums, num1, num2, num3, num4):
            return self.handleCase3(nums, num1, num2, num3, num4)
        else:
            # case 4
            return self.handleCase4(nums)

    def handleCase4(self, nums):
        if 0 in nums:
            return "00:00"
        elif 1 in nums:
            return "11:11"
        else:
            return "22:22"

    def handleCase3(self, nums, num1, num2, num3, num4):
        if num2 != nums[3]:
            inxNum2 = b.bisect(nums, num2, 0, 3)
            return str(num1) + str(nums[inxNum2]) + ":" + str(nums[0]) * 2
        else:
            return str(num1 + 1) + str(nums[0]) + ":" + str(nums[0]) * 2

    def detectCase3(self, nums, num1, num2, num3, num4):
        if num1 == 0:
            return num2 != nums[3] or 1 in nums or 2 in nums
        elif num1 == 1:
            return num2 != nums[3] or 2 in nums
        elif num2 != nums[3]:
            inxNum2 = b.bisect(nums, num2, 0, 3)
            return nums[inxNum2] <= 4
        else:
            return False
