# lineupg.md

## Question:
每天,农夫 John 的N(1 <= N <= 50,000)头牛总是按同一序列排队. 有一天, John
决定让一些牛们玩一场飞盘比赛. 他准备找一群在对列中为置连续的牛来进行比赛.
但是为了避免水平悬殊,牛的身高不应该相差太大.

John 准备了Q (1 <= Q <= 180,000) 个可能的牛的选择和所有牛的身高 (1 <=
身高 <= 1,000,000). 他想知道每一组里面最高和最低的牛的身高差别.

Find the biggest and the smallest number in the line.

## Analysis:
算法思路： 
1）如果数组长度为1，则最大值与最小值相等 
2）如果数组长度为2，则最大值与最小值各位其中一个。 
3）如果数组长度大于2，那么采用二分策略，递归求前一半的最大最小值，与后一半的最大最小值，之后两两比较后的数组的最大最小值。

## Solution1:Python
```Python
#!/usr/bin/env python2.7

def main():
    height =[]
    queries = []

    with open('lineupg2.in', 'r') as fin:
        n, q = map(int, fin.readline().split(' '))
        for i, line in enumerate(fin):
            if i < n:
                height.append(line.strip())
            else:
                queries.append(line.strip())
    #print(queries)

    height = [int(h, 10) for h in height]
    query=[]


    def find(a,i,j,min,max):
        if i >= j - 1:
            if a[i] > a[j]:
                if min>a[j]:
                    min=a[j]
                if max<a[i]:
                    max=a[i]
                return min,max
            else:
                if min > a[i]:
                    min = a[i]
                if max < a[j]:
                    max = a[j]
                return min,max

        else:
            mid = int((i + j) / 2)
            tmpmin,tmpmax=find(a, i, mid, min,max)
            min,max=find(a, mid + 1, j, min,max)
            min = tmpmin if tmpmin < min else min
            max = tmpmax if tmpmax > max else max
            return min,max

    for q in queries:
        a=q.split(' ')
        l=[]
        for i in a:
            l.append(int(i))
        query.append(l)
    fout = open('lineupg.out', 'w')
    for q in query:
        l = q[0] - 1
        r = q[1]-1
        min,max=find(height,l,r,100000,-100000)
        #import pdb;pdb.set_trace()
        #print (max,min)
        ans = max-min
        print(ans)
        fout.write(str(ans) + '\n')

if __name__ == '__main__':
    main()
```


## Solution2:C++
```C
#include <iostream>
#include <fstream>
#include <string>

using namespace std;



void max_min(int *num,int l,int r,int &maxnum,int &minnum)  
{  
    if(l==r)            //数组只有一个元素  
    {  
        maxnum=num[l];  
        minnum=num[l];  
        return;  
    }  
    if(l+1==r)          //数组有两个元素  
    {  
        if(num[l]>num[r])  
        {  
            maxnum=num[l];  
            minnum=num[r];  
        }  
        else  
        {  
            maxnum=num[r];  
            minnum=num[l];  
        }  
        return;          //确定最大最小值之后必须返回，否则将进入死循环。  
    }  
    int m =(l+r)/2;  
    int lmax,lmin;  
    max_min(num,l,m,lmax,lmin); //递归求左半部分最大最小值  
  
    int rmax,rmin;  
    max_min(num,m,r,rmax,rmin); //递归求右半部分最大最小值  
  
    maxnum = max(lmax,rmax);  
    minnum = min(lmin,rmin);    //总的最大最小值  
}  

int main()
{

	freopen("lineupg.in", "r", stdin);
	freopen("lineupg.out", "w", stdout);
	int n, q;
	scanf("%d %d", &n, &q);
	//cout<<n<<endl;
	//cont<<q<<endl;

	int height[n];
	int i = 0;
	while (i < n) {
		scanf("%d", &height[i]);
		//cout<<height[i]<<endl;
		i++;
	}

	int a[q][2];
	i = 0;
	while (i < q) {
		scanf("%d %d", &a[i][0], &a[i][1]);
		//cout<<a[i][0]<<endl;
		i++;
	}

	int maxnum,minnum;
	i = 0;
	int diff;
	while (i < q) {
		max_min(height, a[i][0]-1, a[i][1]-1, maxnum, minnum);
		diff = maxnum - minnum;
		printf("%d\n",diff);		
		i++;
	}  
}
```

## Analysis: RMQ问题：
这道题是range minimum query RMQ问题：
A1,A2,...An 设计一个数据结构，支持查询操作Query(L,R) 计算min{Al,Al+1...AR}
最常见的方法是Tarjan的sparse-table
预处理O(nlogn) 查询只需要O(1)的时间
递推的方法
d(i,j)=min{d(i,j-1),d(i+2^j-1,j-1)}
对于查询操作，K使得2^k<R-L+1的最大整数
L开头R结尾的两个长度为2^K的区间合起来覆盖了查询区间[L,R] 


## Solution3:RMQ (SPARSE - TABLE)：
```
#include <iostream>
#include <fstream>
#include <string>
#include<iostream> 
#include<algorithm>

using namespace std;

int d[50000][20];
int p[50000][20];

void RMQ_init(int A[], int n ) {
    for (int i = 0; i < n; i++) d[i][0] = A[i];
    for (int j = 1; (1<<j) <= n; j++)
        for(int i = 0; i+(1<<j) -1 < n; i++)
            d[i][j]=min(d[i][j-1],d[i+(1<<(j-1))][j-1]);
}
void RMQ_initi(int A[], int n) {
    for (int i = 0; i < n; i++) p[i][0] = A[i];
    for (int j = 1; (1<<j) <= n; j++)
        for(int i = 0; i + (1<<j) - 1 < n; i++)
            p[i][j]=max(p[i][j-1],p[i+(1<<(j-1))][j-1]);
            
}

int RMQ(int L, int R ) {
    int k = 0;
    while((1<<(k+1)) <= R-L+1 ) k++;
    return max(p[L][k], p[R-(1<<k)+1][k])-min(d[L][k],d[R-(1<<k)+1][k]);
}
int main()
{

    freopen("lineupg.in", "r", stdin);
    freopen("lineupg.out", "w", stdout);
    int n, q; 
    scanf("%d %d", &n, &q);
    int height[n];
    int i = 0;
    while (i < n) {
        scanf("%d", &height[i]);
        i++;
    }
    int a[q][2];
    i = 0;
    while (i < q) {
        scanf("%d %d", &a[i][0], &a[i][1]);
        i++;
    }
    RMQ_init(height, n);
    RMQ_initi(height, n);
    i = 0;
    int diff;
    while (i < q) {
        diff=RMQ(a[i][0]-1, a[i][1]-1);
        printf("%d\n",diff);        
        i++;
    }
}
```
