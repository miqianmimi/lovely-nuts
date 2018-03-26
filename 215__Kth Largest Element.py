class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        print(nums[len(nums)-k])
        return (nums[len(nums)-k])

    def findKthLargest2(self,nums,k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot=nums[0]
        left=[l for l in nums if l<pivot]
        equal=[e for e in nums if e==pivot]
        right=[r for r in nums if r>pivot]

        if k<=len(right):
            return self.findKthLargest2(right,k)
        elif (k-len(right))<=len(equal):
            return equal[0]
        else:
            return self.findKthLargest2(left,k-len(right)-len(equal))
