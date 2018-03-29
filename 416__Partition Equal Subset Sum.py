class Solution(object):
    def canPartition(self, nums):
        nums.sort(reverse=True)
        def helper(start, target):         # Here path is not needed
            if target < 0: return
            elif target == 0: return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]): return True
            return False

        return False if sum(nums)%2 else helper(0, sum(nums)/2)

#DFS算法
#太慢
class Solution2(object):
    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2.)  in possible_sums


    #算出所有可能的解
    #看是不是SUM/2在里面