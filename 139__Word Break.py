class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        f=[]
        f.append(True)
        for i in range(len(s)):
            f.append(False)

#abcde
#[]=True
#a=True
#ab=[a]:True + b
#f[i]=True

#first dp
        i=1
        while i <=len(s):
            #i=4,i=8
            print(i)
            for string in wordDict:
                if len(string) <=i:#string=leet/code=4
                    if f[i-len(string)]:
                        if s[i-len(string):i]==string: #s[0]True S[0:4]==string
                            f[i]=True
                            break
            i=i+1
        print (f)
        return f[len(s)]

        
#second dp
        i=1
        while i<=len(s):
            j=0
            while j<i:
                if f[j] and s[i-j:i] in wordDict:
                    f[i]=True
                    break
                j=j+1
            i=i+1
        return f[len(s)-1]