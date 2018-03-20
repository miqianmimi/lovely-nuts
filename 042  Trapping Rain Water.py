class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        print(height)
        if height==[]:
            return 0
        max = 0
        res = 0
        container =[0]*len(height)
        #print (container)
        for i in range(len(height)):
            container[i]=max
            max =max if max>height[i] else height[i]
        #print(container)

        max = 0
        for i in range(len(height)-1,-1,-1):
            print(len(height))
            print(i)
            container[i] =max if max<container[i] else container[i]
            max = max if max>height[i] else height[i]
            res += container[i]-height[i] if container[i]-height[i]>0 else 0
        #print(container)
        return res

a=Solution()
b=a.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(b)

#Find maximum height of bar from the left end upto an index i in the array left_max.
#Find maximum height of bar from the right end upto an index i in the array right_max.
#Iterate over the \text{height}height array and update ans:
#Add min(max_left[i],max_right[i])−height[i] to ansans