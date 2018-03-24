class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #动态规划
        #前两天是：1-7=-6 (max difference)
        #第三天是：max([3]-min(1,2),-6)=4
        #第四天是：max([4]-min(1,2,3),4)=4
        #第五天是：max([5]-min(1,2,3,4),4)=5
        if prices==[]:
            return 0
        currentmaxdifference=0
        min=prices[0]
        for i,j in enumerate(prices):
            if prices[i]<min:
                min=prices[i]
            currentmaxdifference=max(prices[i]-min,currentmaxdifference)
        return currentmaxdifference