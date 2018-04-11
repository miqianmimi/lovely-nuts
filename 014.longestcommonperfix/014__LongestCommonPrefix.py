class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if strs == [""]:
            return ""
        print(strs)
        print(zip(*strs))
        for i in zip(*strs):
            print(i)
        for i, letter in enumerate(zip(*strs)):
            print(letter)
            print(set(letter))
            if len(set(letter)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

a=Solution()
b=a.longestCommonPrefix(["abcd","abcdef","abc","ade"])