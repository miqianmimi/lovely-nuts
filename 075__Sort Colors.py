class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        List = [0, 0, 0]
        for i in nums:
            if i == 0:
                List[0] += 1
            elif i == 1:
                List[1] += 1
            elif i == 2:
                List[2] += 1
        print(List)

        i = 0
        while i < List[0]:
            nums[i] = 0
            i = i + 1
        while i < List[0] + List[1]:
            nums[i] = 1
            i = i + 1
        while i < List[0] + List[1] + List[2]:
            nums[i] = 2
            i = i + 1
        print(nums)