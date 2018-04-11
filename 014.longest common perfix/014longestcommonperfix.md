# 14. Longest Common Prefix
* Write a function to find the longest common prefix string amongst an array of strings.

### example:
```
"abcdefg"
"abcdefghijk"
"abcdfghijk"
"abcef"
上面的字符串数组的最长公共前缀就是"abc"。
```

### Analysis1:
第一步：找出该字符串数组中的最短字符串的长度l及其序列。
第二步：用for循环从第一个字符串到最后一个字符串作比较。具体步骤如下：
* （1）外层for循环长度从l一直到0
* （2）初始result为最短字符串的前L个字符
* （3）内层for循环中用j表示字符串数组的索引，依次递增.
*  (4) j==len的时候，遍历完成，更新result.

### Solution1:
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if strs==[""]:
            return ""
        lenm=10**5
        s=''
        for i in strs:
            if len(i)<lenm:
                lenm=len(i)
                s=i
        n=len(strs)
        for k in range(lenm,-1,-1):
            m=0
            for p in range(n):
                if strs[p][:k]==s[:k]:
                    continue
                else:
                    m+=1
                    break
            if m==0:
                result=s[:k]
                break
        return (result)
```

zip函数可以把[1,2,3][4,5,6]->[(1,4),(2,5),(3,6)]
zip(/asterisk ab)则是一个反过程
set(’abcd')函数可以->[‘a’,'b','c','d'] 找到序列里面用过的字符。

### Solution2:
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if strs==[""]:
            return ""
        print(strs)
        print(zip(*strs))
        for i ,letter in enumerate(zip(*strs)):
            if len (set(letter))>1:
                return strs[0][:i]
        else:
            return min(strs)
```
