class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            dict.setdefault(i,0)
            dict[i]+=1
        print(dict)
        print(dict.keys())
        a=sorted(dict.items(), key=lambda  x:x[1], reverse=True)
        print(a)
        return(a[0][0])