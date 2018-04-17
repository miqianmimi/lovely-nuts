class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return (0)
        for i,j in enumerate(haystack):
            if j==needle[0]:
                if haystack[i:i+len(needle)]==needle:
                    return (i)
        return ( -1 )