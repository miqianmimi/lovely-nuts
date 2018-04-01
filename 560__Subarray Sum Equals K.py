class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #DP
        li=[]
        li.append(0)
        for i in range(len(nums)):
            c=0
            for j in range(i,-1,-1):
                if sum(nums[j:i+1])==k:
                    c=c+1
            li.append(li[i]+c)
        #print(li)
        return li[-1]


class Solution2(object):
    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #DP
        count = collections.Counter()
        count[0] = 1
        #print(count)
        ans = su = 0
        for x in nums:
            su += x
            #print(su)
            ans += count[su-k]
            #print(ans)
            count[su] += 1
            #print(count)
        return ans
    #计算到当前位置的累加和，sum 然后循环n次，每一次都是计算以i[n]为结尾的字符串有木有和==需要的值，