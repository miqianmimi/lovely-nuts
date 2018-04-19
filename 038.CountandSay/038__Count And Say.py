class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        L = []
        L.append(1)
        for i in range(2, n + 1):
            s = L[i - 2]
            d = []
            s = str(s)
            t = 0
            while t <= len(s) - 1:  # 0,1
                count = 1
                if t < len(s) - 1:  # t=0
                    while s[t] == s[t + 1]:  # 不相等2！=1
                        count = count + 1
                        t = t + 1
                        if t == len(s) - 1:
                            break
                    d.extend([count, s[t]])
                else:
                    d.extend([1, s[t]])
                t = t + 1
            ans = ''
            for i in d:
                ans += str(i)
            L.append(ans)
        return (L[-1])

