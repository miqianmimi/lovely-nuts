# 43. Multiply Strings

## Question:

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

## Example:

Input: num1 = "2", num2 = "3"
Output: "6"

## Analysis:

`要注意的是高位是i+j,低位是i+j+1`

* 1. 两数相乘，结果的长度不会大于两数长度和m + n，所以一开始我们开一个int[] res = new int[m + n]
* 2. 接下来对num1和num2做一个双重循环从后向前遍历
* 2.1.当前的 digit1 = num1.charAt(i) - '0'，  digit2 = num2.charAt(j) - '0'
* 2.2.这时我们可以更新当前res[i + j + 1]的这个位置为原来存在这一位置上的值再加上新的值digits 1 * digit2，简略一下就是 res[i + j + 1] += digits 1 * digit2 
* 2.3.接下来根据res[i + j + 1]的新值，我们可以更新高一位的res[i + j]，  res[i + j] += res[i + j + 1] / 10，就是本来的值加上进位 
* 2.4.最后我们再用res[i + j + 1] %= 10求出这一位置进位后剩下的digit
* 3. 求出res数组之后我们可以建立一个StringBuilder sb，来从头遍历数组，求出最终结果
* 3.1.要注意的是当sb.length() == 0并且res[i] = 0时，这时候是开头的0值，需要跳过
* 3.2.假如遍历完毕以后sb.length()依然等于0， 我们返回"0"

Time Complexity - O(mn)，  Space Complexity - O(m + n)


## Solution:
```
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1=len(num1)
        l2=len(num2)
        i=l1-1 #0
        j=l2-1 #1
        res=[]
        for kk in range(i+j+2): #3
            res.append(0)
        while j>=0:
            a=int(num2[j])
            i=l1-1
            while i>=0:
                b=int(num1[i])
                temp=a*b
                res[i + j + 1] += a*b
                res[i + j] += int( res[i + j + 1] / 10)
                res[i + j + 1] %= 10
                i=i-1
            j=j-1
        s=''
        t=0
        if set(res)==set([0]):
            return ("0")
        if res[t]==0:
            while res[t]==0:
                t=t+1     
        while t<len(res):
            s=s+str(res[t])
            t=t+1
        return (s)
```

## 本题关键：
现在这个做法时间复杂度是O(MN)

[分治算法](https://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741370.html) 

可以把复杂度弄到O(N^1.5)

[FFT傅里叶变换](https://www.zybuluo.com/397915842/note/37965)

可以把复杂度变为O(N LOG N)

### python divide and conquer
```
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

```

## reduce 函数：
* python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
```
    def myadd(x,y):  
        return x+y  
    sum=reduce(myadd,(1,2,3,4,5,6,7))  
    print sum  
```

## C++ FFT:
```
string multiply(string num1, string num2) {
    
    int l1 = num1.size(), l2 = num2.size(); 
    int d = max(l1, l2) / 5 + 1; 
    int m = 1; 
    while (m < d) m <<= 1; 
    m <<= 1;
    
    complex *a=new complex[m+1];
    complex *b=new complex[m+1];
    
    memset(a, 0, (m + 1)*sizeof(complex)); 
    memset(b, 0, (m + 1)*sizeof(complex)); 
    int la = 0; 
    for (int i = l1 - 1; i >= 0; i -= 5) { 
        int tmp = 0; 
        for (int j = i - 4; j <= i; ++j) { 
            if (j < 0) continue; 
            tmp = tmp * 10 + num1[j] - '0'; 
        } 
        a[la++] = complex(tmp, 0); 
    } 

    int lb = 0; 
    for (int i = l2 - 1; i >= 0; i -= 5) { 
        int tmp = 0; 
        for (int j = i - 4; j <= i; ++j) {
            if (j < 0) continue; 
            tmp = tmp * 10 + num2[j] - '0'; 
        } 
        b[lb++] = complex(tmp, 0);
    } 

    int l = max(la, lb);
    int n = 1; 
    while (n < l) n <<= 1; 
    n <<= 1;
    
    long long *ans=new long long[n+10];
    
    fft(a, n, 0); 
    fft(b, n, 0); 
    for(int i = 0; i < n; i++) a[i] = a[i] * b[i]; 
    fft(a, n, 1); 

    ans[0] = 0; 
    for (int i = 0; i < n; ++i) { 
        ans[i+1] = 0; 
        ans[i] += (long long)(a[i].x + 0.5); 
        ans[i+1] += ans[i] / 100000; 
        ans[i] %= 100000; 
    } 
    while (ans[n]) {
        ans[n+1] = ans[n] / 100000; 
        ans[n] %= 100000; 
        ++n; 
    } 
    while (n > 1 && ans[n-1] == 0) --n; 


    stringstream s;
    for(int i = n - 1; i >= 0; --i){
        s << (int)ans[i];
        s << setw(5) << setfill('0');
    }
    
    delete[] a;
    delete[] b;
    delete[] ans;
    return s.str();
}

const double pi = acos(-1.0);

struct complex { 
    double x, y; 
    complex(): x(0), y(0) {} 
    complex(double _x, double _y): x(_x), y(_y) {} 

    friend complex operator +(const complex &a, const complex &b) { 
        return complex(a.x + b.x, a.y + b.y); 
    } 
    friend complex operator -(const complex &a, const complex &b) { 
        return complex(a.x - b.x, a.y - b.y); 
    } 
    friend complex operator *(const complex &a, const complex &b) { 
        return complex(a.x * b.x - a.y * b.y, a.x * b.y + a.y * b.x); 
    } 
    friend complex operator /(const complex &a, const double &b) { 
        return complex(a.x / b, a.y / b); 
    }
};
inline complex conj(const complex &a) { 
    return complex(a.x, -a.y); 
}
 
void fft(complex *a, int n, bool inv) {
    complex *w=new complex[n+1];
    int *rv=new int[n+1];
    int bits=-1;
    int _bit = 0; 
    for(int i = 0; i < 30; ++i) if (n & 1 << i) _bit = i; 
    if (_bit != bits) { 
        bits = _bit; 
        rv[0] = 0; 
        rv[1] = 1; 
        for(int st = 1; st < bits; ++st) { 
            int k = 1 << st; 
            for(int i = 0; i < k; ++i) { 
                rv[i+(1<<st)] = rv[i] << 1 | 1; 
                rv[i] <<= 1; 
            } 
        } 
        for(int i = 0; i < 1 << bits; ++i) 
            w[i] = complex(cos(2.0 * pi * i / n), sin(2.0 * pi * i / n)); 
    } 
    for(int i = 0; i < n; i++) 
        if (rv[i] <= i) swap(a[i], a[rv[i]]); 
    for(int d = n >> 1, st = 2; d > 0; d >>= 1, st <<= 1) { 
        int o = st >> 1; 
        for (int j = 0; j < o; ++j) { 
            complex wi = (inv ? conj(w[j*d]) : w[j*d]); 
            for (int i = j; i < n; i += st) { 
                int k = i + o; 
                complex u = a[i], v = a[k] * wi; 
                a[i] = u + v; 
                a[k] = u - v; 
            } 
        } 
    } 
    if (inv) for(int i = 0; i < n; ++i) a[i] = a[i] / n;
    
    delete[] w;
    delete[] rv;
}
```
