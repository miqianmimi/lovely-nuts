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
{	freopen("lineupg.in", "r", stdin);
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