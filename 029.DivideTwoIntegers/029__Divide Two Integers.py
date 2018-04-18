class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647
        if divisor < 0 and dividend > 0:
            divisor = -divisor
            a = -1
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            a = -1
        elif divisor < 0 and dividend < 0:
            divisor = -divisor
            dividend = -dividend
            a = 1
        else:
            a = 1
        m = 1
        p = divisor
        ret = 0

        cingle = [p]
        while (p <= dividend):
            p = p + p
            m = m + m
            cingle.append(p)

        sum = 0
        print(cingle)
        print("m", m)
        j = len(cingle) - 1
        while j >= 0:
            if (sum + cingle[j] <= dividend):
                ret += m
                sum += cingle[j]
            # m=m/2
            m >>= 1
            j = j - 1

        return (ret * a)