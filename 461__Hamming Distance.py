class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=bin(x)
        b=bin(y)
        m=len(a)-2
        n=len(b)-2
        if m>n:
            T=m
            a=a[2:]
            b=b[2:]
            for i in range(m-n):
                b='0'+b
        else:
            T=n
            a=a[2:]
            b=b[2:]
            for i in range(n-m):
                a='0'+a
        print(a,b)
        count=0
        for i in range(T):
            count=count+1 if a[i]!=b[i] else count
        return count
    def hammingDistancew(self, x, y):

        return bin(x ^ y).count('1')
