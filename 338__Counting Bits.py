class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        def get(num):
            list = []
            count = 0
            while num > 0:
                if num % 2 == 0:
                    list.append(0)
                    num = num / 2
                elif num % 2 == 1:
                    # print(num)
                    list.append(1)
                    count = count + 1
                    num = (num - 1) / 2
            return count

        t = []
        t.append(0)
        for i in range(1, num + 1):
            a = get(i)
            t.append(a)
        print(t)
        return (t)

    def countBits2(self,num):
        ret=[0]*(num+1)
        i=1
        while i<=num:
            ret[i]=ret[i/2]+i%2
            i=i+1
        return ret

    #也就是说i用二进制表示时1出现的次数等于i / 2
    #中1出现的次数加1（如果i用二进制表示时最右边一位为1，否则不加1）



