class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        print(n)
        i=1
        j=n
        max=0
        ilast=1
        jlast=n

            #import pdb;pdb.set_trace()
        while j>i:
            if height[j-1]<=height[i-1]:
                temp=height[j-1]*(j-i)
                j=j-1
                if temp>max:
                    max=temp
                    ilast=i
                    jlast=j+1
                print(i,j)
            elif height[j-1]>height[i-1]:
                temp=height[i-1]*(j-i)
                i = i + 1
                if temp > max:
                    max = temp
                    ilast=i-1
                    jlast=j
                print(i,j)

        return(max)

a=Solution()
C=a.maxArea([1,1])
print(C)



