class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # hash function
        if needle == "":
            return 0

        if len(needle) > 10:
            for i, j in enumerate(haystack):
                if j == needle[0]:
                    if haystack[i:i + len(needle)] == needle:
                        return (i)
            return (-1)

        else:
            ans = self.hashed(needle)
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i] == needle[0]:
                    # print(haystack[i:i+len(needle)])
                    c = self.hashed(haystack[i:i + len(needle)])
                    if c == ans:
                        return (i)
            return (-1)

    def hashed(self, needle):
        base = 12
        l = len(needle)
        ans = 0
        for i, s in enumerate(needle):
            m = base ** (l - 1 - i)
            ans += ord(s) * m
        return ans

