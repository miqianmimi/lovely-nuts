class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = []
        if len(nums) == 0:
            return 0
        maxx.append(nums[0])
        maxherep = maxx[0]
        minherep = maxx[0]
        maxsofar = maxx[0]
        for i in range(1, len(nums)):
            maxhere = (max(max(maxherep * nums[i], minherep * nums[i]), nums[i]))
            minhere = (min(min(maxherep * nums[i], minherep * nums[i]), nums[i]))
            maxsofar = max(maxhere, maxsofar)
            maxherep = maxhere
            minherep = minhere
        print(maxsofar)
        return (maxsofar)
