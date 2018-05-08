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

## Analysis: RMQ解法：
这道题是range minimum query RMQ问题：
A1,A2,...An 设计一个数据结构，支持查询操作Query(L,R) 计算min{Al,Al+1...AR}
最常见的方法是Tarjan的sparse-table
预处理O(nlogn) 查询只需要O(1)的时间
递推的方法
d(i,j)=min{d(i,j-1),d(i+2^j-1,j-1)}
对于查询操作，K使得2^k<R-L+1的最大整数
L开头R结尾的两个长度为2^K的区间合起来覆盖了查询区间[L,R] 


## Solution3:RMQ (SPARSE - TABLE)：
```C
#include <iostream>
#include <fstream>
#include <string>
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

real    0m0.111s

user    0m0.102s

sys 0m0.007s

right!

## Analysis: 线段树：
每次Update操作都需要重新计算d数组，时间无法承受。从上到下，从左到右的顺序给所有结点编号，
左右子结点的编号为2i和2i+1.

根结点是一个长度为2^h的区间，第I层有2^i个结点，每个结点对应一个长度为2^(h-i)的区间，最大编号为h，结点总数为1+2+4+8+...+2^h=2^h+1 -1略小于区间长度的两倍。
当整个区间长度不是2的整数幂的时候，虽然叶子不全在同一层，但树的最大层编号和结点总数仍然能满足上述结论。

在这些线段中，可以拥有附加信息，重头戏，每个结点上记录该线段中所有元素的最小值，

可以用一个数组minv保存这个附加信息,其中minv[o]表示结点o所对应的区间中所有元素的最小值。

[5，8]的编号为3，因此minv[3]=min{A5,A6,A7,A8}

在查询时，我们从根结点开始自顶向下找到待查询线段的左边界和右边界，则夹在中间的所有叶子结点不重复不遗漏地覆盖了整个待查询线段。

虽然树左右都分叉，但每次最多两个结点向下延伸。所以最下方的节点最多2h个，h是最大层编号     我们可以递归得到边界

最后叙述一下建立树的过程，一种方法是每次读入一个元素后修改A[i]=x
设置好每个叶节点的值，自底向上递推即可。

[线段树](http://www.cnblogs.com/TenosDoIt/p/3453089.html)                                                                                               
## Solution4:线段树
```C
#include <iostream>
#include <fstream>
#include <string>
#include<algorithm>
const int MAXNUM = 180000;
const int INF = INT_MAX;
int height[MAXNUM];
using namespace std;
struct SegTreeNode
{
    int minval;
    int maxval;
}segTree[MAXNUM];//定义线段树
void Build(int root,int height[], int istart, int iend){
    if(istart == iend){
        segTree[root].minval = height[istart];
        segTree[root].maxval = height[istart];
        return;
    }
    else{
        int mid = (istart + iend) >> 1;
        Build(root * 2 ,height, istart, mid);
        Build(root * 2 + 1,height, mid+1, iend);
        segTree[root].minval = min(segTree[root * 2 ].minval, segTree[root * 2 + 1].minval);
        segTree[root].maxval = max(segTree[root * 2 ].maxval, segTree[root * 2 + 1].maxval);
    }
}
int Querysmall(int o, int L, int R, int ql, int qr){
    if (ql > R || qr < L)
        return(-1);
    int M = (R + L) / 2 ; 
    if( ql <= L && R <= qr ) return segTree[o].minval;
    int rs1 = Querysmall(o * 2 , L, M, ql, qr);
    int rs2 = Querysmall(o * 2 + 1, M + 1, R, ql, qr) ;
    if ( rs1 == -1 )  
        return(rs2);  
    if ( rs2 == -1 )  
        return(rs1);  
    if ( rs1 <= rs2 )
        return (rs1);
    return (rs2);

}
int Querybig(int o, int L, int R, int ql, int qr){
    if (ql > R || qr < L)
        return(-1);
    int M = (R + L) / 2 ;
    if( ql <= L && R <= qr ) return segTree[o].maxval;
    int rs1 = Querybig(o * 2 , L, M, ql, qr);
    int rs2 = Querybig(o * 2 + 1, M + 1, R, ql, qr) ;
    if ( rs1 == -1 )  
        return(rs2);  
    if ( rs2 == -1 )  
        return(rs1);  
    if ( rs1 >= rs2 )
        return (rs1);
    return (rs2);
}
void updateOne(int root, int nstart, int nend, int index, int addVal)
{
    if(nstart == nend)
    {
        if(index == nstart)
            segTree[root].minval += addVal;
        return;
    }
    int mid = (nstart + nend) / 2;
    if(index <= mid)
        updateOne(root*2+1, nstart, mid, index, addVal);
    else updateOne(root*2+2, mid+1, nend, index, addVal);
    segTree[root].minval = min(segTree[root * 2 + 1].minval, segTree[root * 2 + 2].minval);
}
int main()
{   freopen("lineupg.in", "r", stdin);
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
    Build(1,height,0,n-1);
    i = 0;
    int diff;
    int big;
    int small;
    while (i < q) {
        big = Querybig(1, 0, n - 1, a[i][0] - 1, a[i][1] - 1);
        small = Querysmall(1, 0, n - 1, a[i][0]-1 , a[i][1]-1 );
        //printf("%d\n",big);       
        //printf("%d\n",small);     
        diff = big - small;
        printf("%d\n",diff);        
        i++;
    }
}
```

## 本题关键：暴力遍历一遍; RMQ (SPARSE - TABLE); 以及线段树
