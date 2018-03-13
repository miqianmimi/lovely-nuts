#采用马拉车方法
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        import numpy as np
        def count(s):
            count = 0
            for i in s:
                count = count + 1
            return (count)
        len=count(s)
        P=np.array(len)
        def reversssy(s):
            new = ''
            count = 0
            for i in s:
                count = count + 1
            for i in range(count):
                a = int(count - i - 1)
                new = new + s[a]
            return (new)
        def trans(s):
            new='$'
            for i in range(len):
                new=new+str('#')
                new=new+s[i]
            return str(new+'#')
        news=(trans(s))
        newlen=count(news)
        P=np.array([0]*newlen)
        i=1
        #print(newlen)
        id=0
        mx=0
        resLen = 0
        resCenter = 0

        while i<newlen:
            if mx>i:
                P[i]=min(P[2*id-i],mx-i)
            else:
                P[i]=1
            #print(P)
            if i+P[i]<newlen:
                while(news[i+P[i]]==news[i-P[i]]):
                        P[i]=P[i]+1
                        if i+P[i]==newlen:
                            break
            if i+P[i]>mx :
                mx=i+P[i]-1
                id=i
            i=i+1
        md=max(P)
        id=np.argwhere(P==md)
        id=id[0][0]
        C=news[id-md+1:id+md]
        PAN=''
        for i in C:
            if i!='#':
                PAN=PAN+str(i)
        lii=count(PAN)
        print('最大回文数{PAN},长度为{lii}'.format(PAN=PAN,lii=lii))
        return(PAN)



a = Solution()
b=a.longestPalindrome('babad')
print(b)