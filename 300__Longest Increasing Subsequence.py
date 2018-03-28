class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*(len(nums))
        res=0
        i=0
        while i<len(nums):
            j=0
            while j<i:
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                j=j+1
            res=max(res,dp[i])
            i=i+1
        print(dp)
        return res


#O(n*2)
#对于每一个nums[i]，我们从第一个数再搜索到i，如果发现某个数小于nums[i]，我们更新dp[i]，更新方法为dp[i] = max(dp[i], dp[j] + 1)，即比较当前dp[i]的值和那个小于num[i]的数的dp值加1的大小，



#O(n*logn)
#维护一个数组tail:tail 表示单位长度为1，2，3，4..的连续序列和，最末尾的数是多少。
class Solution2(object):
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
a=Solution()
b=a.lengthOfLIS([-2,-1])
print(b)

