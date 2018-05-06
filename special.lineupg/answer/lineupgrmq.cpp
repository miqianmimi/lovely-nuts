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
