class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = ['A']
        m = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in m.keys():
                if stack.pop() != m[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 1 #最后应该全出来了，为了防止一个']'无法Pop，先藏一个

a=Solution()
b=a.isValid('({[]})')
c=a.isValid('([{[]}])[]')
d=a.isValid('([{[}])[]')

print(b,c,d)
