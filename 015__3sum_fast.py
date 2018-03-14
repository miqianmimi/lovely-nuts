#This is o(n*2) solution which is not good enough.
class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def quicksort(nums):
            if len(nums)<=1:
                return(nums)
            h=nums.pop()
            Left=[]
            Right=[]
            for i in nums:
                if i >=h:
                    Right.append(i)
                else:
                    Left.append(i)
            return quicksort(Left)+[h]+quicksort(Right)
        newnum=quicksort(nums)

        def twoSum(num, target):
            dictx = {}
            for idx, n in enumerate(num, 1):
                rest = target - n
                if rest in dictx:
                    return num[dictx[rest]], num[idx]
                dictx[n] = idx

        def find(newsum):
            fin=[]
            if newsum==[]:
                return([])
            if len(newsum)<=2:
                return([])
            if newsum[0]+newsum[1]+newsum[2]>0:
                return([])
            l=len(newsum)
            if newsum[l-1]+newsum[l-2]+newsum[l-3]<0:
                return([])


            i=0
            while i<=l-3:
                while newsum[i]+newsum[l-1]+newsum[l-2]<0:
                    i=i+1
                while i != 0 and newsum[i] == newsum[i - 1]  and i<=l-3:
                    i=i+1
                    #print(i)
                if newsum[i]+newsum[l-1]+newsum[l-2]==0:
                    fin.append([newsum[i],newsum[l-1],newsum[l-2]])
                else:

                    tmp=0-newsum[i]
                    j=i+1
                    z=l-1
                    while z>j:
                        if newsum[j]+newsum[j+1]>tmp:
                            break
                        if newsum[z]+newsum[z-1]<tmp:
                            break
                        if newsum[j]+newsum[z]>tmp:
                            z=z-1
                        elif newsum[j]+newsum[z]<tmp:
                            j=j+1
                        elif newsum[j]+newsum[z]==tmp:
                            fin.append([newsum[i], newsum[j], newsum[z]])
                            while j<z and newsum[j] == newsum[j+1]:
                                j=j+1
                            while j<z and newsum[z] == newsum[z-1]:
                                z=z-1
                                #print(z)
                            j=j+1
                            z=z-1


                i=i+1
            return(fin)

        b=find(newnum)

        #print(b)
        if b == []:
            return ([])
        else:
            c=[]
            [c.append(i) for i in b if not i in c]
            return(c)

#this is o(n) and good enough
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()#去除重复
        for i, v in enumerate(nums[:-2]): #enumerate 可遍历函数中全部的元素
            #print(nums[:-2])
            #print(i,v) #i是v的序号
            if i >= 1 and v == nums[i-1]: #类似于同类往前进
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                    #print(nums)
                    #print(d) #把需要的值都添加到表里面
                elif x in d: #如果x正好在表里面，那么就是要求的值。
                    res.add((v, -v-x, x))
        #print(d)
        a=map(list,res)
        B=[]
        for i in a:
            B.append(i)
        return (B)
a=Solution()
B=a.threeSum([1,3,-2,1,-3,0,1])
print(B)
