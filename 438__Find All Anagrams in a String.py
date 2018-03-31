from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        re=self.para(p)
        print(re)
        a=len(p)
        li=[]
        for i in range(len(s)-a+1):
            if s[i:i+a] in re:
                li.append(i)
        return li
    def para(self,p):
        pp=[str(c)+str(d) for i,c in enumerate(p)
           for d in self.para(p[:i]+p[(i+1):])] or [str("")]
        return list(set(pp))


    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        res = []
        pCounter = Counter(p)
        #print(pCounter)
        sCounter = Counter(s[:len(p)-1])
        #print(1)
        #print(sCounter)
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window 第三个a+=1
            #print('one')
            #print(sCounter)
            #cOUNTER里面元素一样，就等了
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters
                res.append(i-len(p)+1)   # append the starting index
            #第一个字母-=1
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                #把带0的元素删掉
                #print('two')
                #print(sCounter)
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res


a=Solution()
b=a.findAnagrams2("cbaebabacd","abc")