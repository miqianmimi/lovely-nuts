class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(target,nums,index,path,result):
            if target<0:
                return None
            if target==0:
                result.append(path)
                return
            if target>0:
                for i in range(index, len(nums)):
                    dfs(target-nums[i],nums,i,path+[nums[i]],result)
        result=[ ]
        path=[]
        dfs(target,candidates,0,path,result)
        return result
a=Solution()
b=a.combinationSum([4,3,2,1,7],7)
print(b)

