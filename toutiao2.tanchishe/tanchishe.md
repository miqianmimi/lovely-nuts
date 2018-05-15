# 贪吃蛇蛇

### Question:
小Q最近迷上了一款叫“贪吃蛇蛇”的小游戏，平面上有个数字矩阵，每个单元都是一个整数，有正有负，最开始的时候小Q操纵一条长度为0的蛇蛇从矩阵最左侧任选一个单元格进入地图，蛇每次只能够到达当前位置的右上相邻，右侧相邻和右下相邻的单元格，当蛇蛇到达一个单元格，自身的长度会瞬间加上该单元格的数值任何情况下长度为负，则游戏结束，

小Q是天才，超能力，可以字啊游戏开始时的时候把地图中的某一个结点的值编委相反数，最多只能改一个节点，问小Q在游戏里面，蛇蛇最长长度可以到达多少

### Example:
```
输入：第一行两个整数n,m，表示地图有n行m列
接下来的n行，每行m个整数T(i，j)表示地图中每个单元的值
输出：一个整数，表示蛇的最长的长度

”
4 3 
1 -4 10
3 -2 -1
2 -1 0
0 5 -2

17
```

### Analysis:
首先，同样使用动态规划来算这个问题；
加一维度f[i][j][0]表示没有使用过Q
f[i][j][1]表示一定使用过Q了。
f[i][j][1]从0转移过来表示了。
所以状态转移方程是3个。
若可以使用n+1次魔法的话，2n+1次状态转移方程。
        f[i][j][0] = max(f[i][j][0], f[k][j-1][0] + a[i][j]);

        f[i][j][1] = max(f[i][j][1], f[k][j-1][1] + a[i][j]);
        f[i][j][2] = max(f[i][j][2], f[k][j-1][2] + a[i][j]);

        f[i][j][n] = max(f[i][j][n], f[k][j-1][n] + a[i][j]);

        f[i][j][1] = max(f[i][j][1], f[k][j-1][0] - a[i][j]);
        f[i][j][2] = max(f[i][j][1], f[k][j-1][1] - a[i][j]);

        f[i][j][n] = max(f[i][j][1], f[k][j-1][n-1] - a[i][j]);


### Solution:C++
```C
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int inf = 1<<30;
const int maxn = 100;
int f[maxn][maxn][2];
int a[maxn][maxn];
int n, m ;

int main(){
	freopen("c.in","r",stdin);
	scanf("%d%d\n", &n, &m);
	for (int i = 1; i <= m; i++){
		for(int j = 1; j<= n; j++){
			scanf("%d", &a[i][j])
		}
	}
	for (int i = 0; i <= n; i++){
		for (int j = 0; j <= m; j++){
			f[i][j][0] = f[i][j][1] = -inf
		}
	}
	//动态规划开始
	for (int j = 2; j <= m; j++){
		for (int i = 1; i <= n; i++){
			for (int k = i - 1; k <= i + 1; k++){
				if (k < 1 || k > n) continue;
				f[i][j][0] = max(f[i][j][0], f[k][j-1][0] + a[i][j]);
				f[i][j][1] = max(f[i][j][1], f[k][j-1][0] - a[i][j]);
				f[i][j][1] = max(f[i][j][1], f[k][j-1][1] + a[i][j]);
			}
		}
	}
	int ans = -inf;
	for (int i = 1 ; i <= n; i++){
		ans = max(ans, f[i][m][0]);
		ans = max(ans, f[i][m][1]);
	}
	printf("%d\n", ans);
	return 0;
}
```

### 本题关键：
* 动态规划
* 状态转移方程：怎么用加一个维度，三个状态转移方程来解决特殊情况的问题