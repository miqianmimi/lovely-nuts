class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        def count(s):
            count = 0
            for i in s:
                count = count + 1
            return (count)
        m=count(s)
        if m==0:
            return('')
        if m==1:
            return(s)
        n=numRows
        if n==1:
            return(s)
        if m<=n:
            return(s)
        a=int((m-n)/(n-1))  #6
        b=m-((a+1)*n-a)  #1
        last=''
        if a%2==1:
            c=(a+1)/2
            #print(c)
            c=int(c)
            i=1
            while i<=n: #i从1-n
                if i==1:
                    print(s[1-1])
                    last = last + s[1- 1]
                    j=1
                    while j <=c: #j从0到c=3
                        print(s[1+(2*n-2)*j-1])
                        last=last+s[1+(2*n-2)*j-1]
                        j=j+1
                if i>=2 and i<=1+b:
                    print(s[i - 1])
                    print(i)
                    last = last + s[i - 1]
                    j=1
                    while j<=c:
                        print(s[i+(2*n-2)*(j-1)+(2*n-2*i)-1])
                        last = last + s[i+(2*n-2)*(j-1)+(2*n-2*i)-1]
                        print(s[i+(2*n-2)*(j)-1])
                        last= last + s[i+(2*n-2)*(j)-1]
                        j=j+1
                if i>1+b and i<=n-1:
                    print(s[i - 1])
                    last = last + s[i - 1]
                    j=1
                    while j<=c-1:
                        print(s[i+(2*n-2)*(j-1)+(2*n-2*i)-1])
                        last = last + s[i+(2*n-2)*(j-1)+(2*n-2*i)-1]
                        print(s[i+(2*n-2)*(j)-1])
                        last= last + s[i+(2*n-2)*(j)-1]
                        j=j+1
                    print(s[i+(2*n-2)*(c-1)+(2*n-2*i)-1])
                    last = last + s[i+(2*n-2)*(c-1)+(2*n-2*i)-1]
                if i==n:
                    print(s[n-1])
                    last = last + s[n- 1]
                    j=1
                    while j <=c-1: #j从0到c=2
                        print(s[n+(2*n-2)*j-1])
                        last=last+s[n+(2*n-2)*j-1]
                        j=j+1
                i=i+1
        if a%2==0:
            c=(a)/2
            print(c)
            c=int(c)
            i=1
            while i<=n: #i从1-n
                if i==1:
                    print(s[1-1])
                    last = last + s[1- 1]
                    j=1
                    while j <=c: #j从0到c=3
                        print(s[1+(2*n-2)*j-1])
                        last=last+s[1+(2*n-2)*j-1]
                        j=j+1
                if i>=2 and i<n-b:
                    print(s[i - 1])
                    last = last + s[i - 1]
                    j=1
                    while j<=c:
                        print(s[i+(2*n-2)*(j-1)+(2*n-2*i)-1])
                        last = last + s[i+(2*n-2)*(j-1)+(2*n-2*i)-1]
                        print(s[i+(2*n-2)*(j)-1])
                        last= last + s[i+(2*n-2)*(j)-1]
                        j=j+1
                if i>=n-b and i<=n-1:
                    print(s[i - 1])
                    last = last + s[i - 1]
                    j=1
                    while j<=c:
                        print(s[i+(2*n-2)*(j-1)+(2*n-2*i)-1])
                        last = last + s[i+(2*n-2)*(j-1)+(2*n-2*i)-1]
                        print(s[i+(2*n-2)*(j)-1])
                        last= last + s[i+(2*n-2)*(j)-1]
                        j=j+1

                    print(i+(2*n-2)*(c)+(2*n-2*i)-1)
                    print(s[i+(2*n-2)*(c)+(2*n-2*i)-1])
                    last = last + s[i+(2*n-2)*(c)+(2*n-2*i)-1]
                if i==n:
                    print(s[n-1])
                    last = last + s[n- 1]
                    j=1
                    while j <=c: #j从0到c=1
                        print(s[n+(2*n-2)*j-1])
                        last=last+s[n+(2*n-2)*j-1]
                        j=j+1
                i=i+1
        return(last)



a=Solution()
B=a.convert("PAYPALIS", 3)
print(B)
