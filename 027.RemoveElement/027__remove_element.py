class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        nums.sort()
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
                i = i + 1
            else:
                i = i + 1
                j = j
        nums = nums[:j]
        print(nums)
        return len(nums)




