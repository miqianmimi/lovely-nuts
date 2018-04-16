class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        solution = []
        for x, i in enumerate(nums):
            ntarget = target - i
            for y, j in enumerate(nums[x + 1:]):
                newtarget = ntarget - j
                newpool = nums[x + y + 1 + 1:]
                left = 0
                right = len(nums) - x - y - 1 - 1 - 1
                while left < right:
                    diff = newtarget - newpool[left] - newpool[right]
                    if diff == 0:
                        if [nums[x], nums[x + 1 + y], nums[x + 1 + y + left + 1],nums[x + 1 + y + right + 1]] not in solution:
                            solution.append([nums[x], nums[x + 1 + y], nums[x + 1 + y + left + 1], nums[x + 1 + y + right + 1]])
                        left = left + 1
                        right = right - 1
                    if diff > 0:
                        left = left + 1
                    if diff < 0:
                        right = right - 1
        return solution


