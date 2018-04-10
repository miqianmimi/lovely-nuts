class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m = str(x)
        a = ''
        for i in m:
            a = i + a
        print(a)

        if a[-1] == '-':
            return False
        a = int(a)
        print(a)
        if a - x == 0:
            return True
        else:
            return False


