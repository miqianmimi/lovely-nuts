class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        F = [0, nums[0], max(nums[0], nums[1])]
        i = 3
        while i <= len(nums):
            temp = max(F[i - 1], F[i - 2] + nums[i - 1])
            F.append(temp)
            i = i + 1
        return F[-1]
