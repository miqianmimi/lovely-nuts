class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        i=0
        reach=0
        while i<n and i<=reach:
            reach=max(i+nums[i],reach)
            print(reach,i)
            i=i+1
        print(i,n)
        print(i==n)
        return i==n