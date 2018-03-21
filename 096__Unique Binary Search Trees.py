class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G=[] # equals the num of numTrees
        G.extend([1,1])
        #G[N]=sum G[N-I]*G[I]

        for j in range(1,n):
            count = 0
            i=0
            while i<=j:
                count=count+G[i]*G[j-i]
                i=i+1
            G.append(count)

        print(G)
        print (G[n])
        return (G[n])

a=Solution()
b=a.numTrees(3)
print(b)