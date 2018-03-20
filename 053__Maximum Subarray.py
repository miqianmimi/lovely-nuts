class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=['-inf']*n
        dp[0]=nums[0]
        max=int(dp[0])
        for i in range(1,len(nums)):
            dp[i]=nums[i]+dp[i-1] if dp[i-1]>0 else nums[i]
            max=max if int(dp[i])<max else int(dp[i])
        print(dp)

        return(max)

a=Solution()
b=a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(b)