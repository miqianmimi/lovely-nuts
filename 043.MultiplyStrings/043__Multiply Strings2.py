class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        i = l1 - 1  # 0
        j = l2 - 1  # 1
        res = []
        for kk in range(i + j + 2):  # 3
            res.append(0)
        while j >= 0:
            a = int(num2[j])
            i = l1 - 1
            while i >= 0:
                b = int(num1[i])
                temp = a * b
                res[i + j + 1] += a * b
                res[i + j] += int(res[i + j + 1] / 10)
                res[i + j + 1] %= 10
                i = i - 1
            j = j - 1

        s = ''
        t = 0
        print(set(res))
        if set(res) == set([0]):
            return ("0")
        print(res)

        if res[t] == 0:
            while res[t] == 0:
                t = t + 1

        while t < len(res):
            s = s + str(res[t])
            t = t + 1

        return (s)