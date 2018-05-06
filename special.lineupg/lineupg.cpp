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
	int n，q;
	scanf("%d %d", &n, &q);
	cout<<n<<endl;
	cout<<q<<endl;

	int height[n];
	int i = 0;
	while (i < n) {
		scanf("%d", &height[i]);
		cout<<height[i]<<endl;
		i++;
	}

	int a[q][2];
	i = 0;
	while (i < q) {
		scanf("%d %d", &a[i][0], &a[i][1]);
		cout<<a[i][0]<<endl;
		i++;
	}

	int maxnum,minnum;
	i = 0；
	int diff;
	while (i < q) {
		max_min(height, a[i][0]-1, a[i][1]-1, maxnum, minnum);
		diff = maxnum - minnum;
		printf("%d \n",diff);		
		i++;

	}

   
}
