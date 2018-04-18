# 29. Divide Two Integers

### Question:
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.

### Example:
```
Input: dividend = 10, divisor = 3
Output: 3
```

### Analysis:
既然不能直接累加，那么还有什么新的方法呢？
二进制是可以表示所有数字的。那么在这题中使用二进制来逼近是较为迅速的办法。

假定商是l，那么l一定可以用二进制来表示，也即2的幂和，5=2^2+2^1。那么所需要做的也就是累加除数与2的幂次乘积，直至刚好超过被除数，然后从最大的次幂开始计算，如果当前的和加上该次幂大于被除数，那么放弃该次幂，如果加上该次幂仍然小于被除数，那么就加上该次幂。

举个例子，假设除数为3，被除数为16，那么商应该是5。我们从2的0次幂与除数的乘积也即20x3=3开始，幂次逐渐增加，直至超过被除数。可以看出，当幂次达到2时刚好超过16（3x20+3x21+3x22=21>16）。那么从3x22开始往下累加，3x22=12>16，那么记录下22=4。再看3x21，发现3x22+3x21=18>16，因此略过21=2。再看3x20，发现发现3x22+3x20=15<16，那么将20=1记录下。次幂累加结束，计算一下商，分别记录了4和1，因此结果4+1=5，此答案也即为最终的商。

* 防止溢出

算法大概的思路差不多讲完了，还需要注意的就是边界问题，只有一个边界特例需要考虑Integer.MIN_VALUE和-1。此时的结果超过了Integer所能表示的最大范围，因此需要特殊处理。其次，为了简单起见，我们将除数和被除数的符号进行记录，然后将其转换为正数进行计算，这也涉及到溢出的问题，Integer.MIN_VALUE转换为正数之后会超过32位Integer所能表示的范围，因此在代码中使用long类型进行计算防止溢出。
**因为负数最大能表示2\*\*31此方，正数是2\*\*31-1，所以负MAX/负1得2\*\*31>最大的正数，所以要特别处理成2\*\*31-1**

### Solution:
```+python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if(dividend == -2147483648 and divisor == -1):
            return 2147483647
        if divisor<0 and dividend>0:
            divisor=-divisor
            a=-1
        elif dividend<0 and divisor>0:
            dividend=-dividend
            a=-1
        elif divisor <0 and dividend <0:
            divisor=-divisor
            dividend=-dividend
            a=1
        else:
            a=1  
        m=1
        p=divisor
        ret=0

        cingle=[p]
        while (p<=dividend):
            p=p+p
            m=m+m
            cingle.append(p)
            
        sum=0
        print(cingle)
        print("m",m)
        j=len(cingle)-1
        while j>=0:
            if (sum + cingle[j] <= dividend):
                ret += m
                sum +=cingle[j]
            #m=m/2
            m>>=1
            j=j-1
        
        return(ret*a)
```

### 本题关键：
* ***防止溢出的问题很重要***@
* `还有将思路从除法转变为加法，用一个2的幂次和去逼近的想法很关键！`
