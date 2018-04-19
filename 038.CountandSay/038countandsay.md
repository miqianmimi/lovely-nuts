# 38. Count and Say

### * Question:
The count-and-say sequence is the sequence of integers with the first five terms as following:
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

### Example:
```
Input: 1
Output: "1"
```

### Analysis:
题意是n=1时输出字符串1；n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；n=3时，由于上次字符是11，有2个1，所以输出21；n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。依次类推，写个countAndSay(n)函数返回字符串。


### Answer:
```
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        L=[]
        L.append(1)
        for i in range(2,n+1):
            s=L[i-2]
            d=[]
            s=str(s)
            t=0
            while t<=len(s)-1: #0,1
                count=1
                if t<len(s)-1: #t=0
                    while s[t] ==s[t+1]: #不相等2！=1
                        count=count+1
                        t=t+1
                        if t==len(s)-1:
                            break
                    d.extend([count,s[t]])  
                else:
                    d.extend([1,s[t]])
                t=t+1
            ans=''
            for i in d:
                ans+=str(i)
            L.append(ans)
        return(L[-1])
```

###  题目关键
*  递归法？       
        