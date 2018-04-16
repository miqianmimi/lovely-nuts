class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        l = len(nums)
        if nums == []:
            return (0)
        while (i < l and j < l):
            if nums[i] == nums[j]:
                i = i + 1
            else:
                nums[j + 1] = nums[i]
                i = i + 1
                j = j + 1
        a = nums[:j + 1]
        print(a)
        return (j + 1)

