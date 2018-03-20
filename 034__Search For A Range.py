class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return([-1,-1])
        if len(nums)==1:
            if nums[0]==target:
                return([0,0])
            else:
                return([-1,-1])
        a=0
        b=len(nums)-1
        def search(a,b,nums,target,list,result):
            e=int((a+b)/2)
            if a<=b:
                if nums[e]==target:
                    c=search(a,e-1,nums,target,list,result)
                    d=search(e+1,b,nums,target,list,result)
                    return c+[e]+d
                elif nums[e]>target:
                    return search(a,e-1,nums,target,list,result)
                elif nums[e]<target:
                    return search(e+1,b,nums,target,list,result)
            elif a > b:
                result=list
                return(result)
        list=[]
        result=[]
        result=search(a,b,nums,target,list,result)
        if result==[]:
            return([-1,-1])
        else:
            return([result[0],result[-1]])

a=Solution()
b=a.searchRange([5, 7, 7, 7, 9, 10],8)
print(b)