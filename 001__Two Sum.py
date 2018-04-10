class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = []
        for i in nums:
            c.append(target - i)
        print(c)
        for i, j in enumerate(nums):
            if j in c and i != c.index(j):
                return (i, c.index(j))


