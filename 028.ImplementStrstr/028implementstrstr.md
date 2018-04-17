# 28. Implement Strstr()

### Question:
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Example:
```
Input: haystack = "hello", needle = "ll"
Output: 2
```
### Analysis:
判断一个字符串是否是另一个字符串的子串
* [1]这个题目最经典的算法应该是KMP算法,KMP算法是最优的线性算法，很难在面试的短时间里面完整正确的实现。所以一般在面试中并不要求实现KMP算法。
* [2]brute force的算法，假设原串的长度是n，匹配串的长度是m。思路很简单，就是对原串的每一个长度为m的字串都判断是否跟匹配串一致。总共有n-m+1个子串，所以算法时间复杂度为O((n-m+1)*m)=O(n*m)，
* [3]rolling hash，想具体了解的朋友可以参见Rolling hash - Wikipedia。基本思想是用一个hashcode来表示一个字符串，为了保证hash的唯一性，我们用比字符集大的素数为底，以这个素数的幂为基。举例来说，字符集是小写字母集，取素数29为底。比如字符串“abacd",转化为hashcode=1+2\*29+1\*29^2+3\*29^3+4\*29^4。然后是如何在前进一步的时候计算新的hashcode，比如匹配串是原串是”abacde“，匹配串长度为5，根据以上的方法计算”abacd“的hashcode=h，那么下一步”bacde“的hashcode=h/29+5\*29^4。
这是一个constant的操作，所以检测所有子串的时间复杂度只需要O(m+n-m)=O(n)



### Solution1:brute force
```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        for i,j in enumerate(haystack):
            if j==needle[0]:
                if haystack[i:i+len(needle)]==needle:
                    return (i)
        return (-1)
```

### Solution2: hash function
```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #hash function 
        if needle=="":
            return 0

        if len(needle)>10:
            for i,j in enumerate(haystack):
                if j==needle[0]:
                    if haystack[i:i+len(needle)]==needle:
                        return (i)
            return (-1)
        
        else:
            ans=self.hashed(needle)
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i]==needle[0]:
                    #print(haystack[i:i+len(needle)])
                    c=self.hashed(haystack[i:i+len(needle)])
                    if c==ans:
                        return (i)
            return(-1)
    def hashed(self,needle):
        base=12
        l=len(needle)
        ans=0
        for i,s in enumerate(needle):
            m=base**(l-1-i)
            ans+=ord(s)*m
        return ans
```

### Solution3:
* Brute Force;Rolling Hash;KMP;
* 不是特别长的字符串，没必要用KMP和rolling hash法，KMP要有冗长的next创建过程。
* 所以在一些小规模的计算中，运算用时反而不如暴力算法来得快。



