from functools import reduce
class Solution(object):
    def multiply(self, num1, num2):

        if not num1 or not num2 or num1 == '0' or num2 == '0': return '0'
        if len(num1) <5 and len(num2) < 5:
            return str(int(num1)*int(num2))
        else:
            a,b,c,d=num1[:len(num1)//2], num1[len(num1)//2:],num2[:len(num2)//2], num2[len(num2)//2:]
            t1 = self.multiply(a,c) + '0' * (len(d)+len(b))
            t2 = self.multiply(b,c) + '0' * len(d)
            t3 = self.multiply(a,d) + '0' *len(b)
            t4 = self.multiply(b,d)
            return reduce(self.str_add, [t1,t2,t3,t4])

    def str_add(self, str1, str2):
        return str(int(str1) + int(str2))