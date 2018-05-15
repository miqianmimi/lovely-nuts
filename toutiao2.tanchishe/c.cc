#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int inf = ~0u>>1;
const int maxn = 1020;
int f[maxn][maxn][2];
int a[maxn][maxn];
int n, m;

int main() {
  freopen("c.in", "r", stdin);
  scanf("%d%d\n", &n, &m);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++){
      scanf("%d", &a[i][j]);
      //printf("%d\n", a[i][j]);
    }
  
  for (int i = 0; i <= n; i++)
    for (int j = 0; j <= m; j++)
      f[i][j][0] = f[i][j][1] = -inf;

  for (int i = 1; i <= n; i++) {
    f[i][1][0] = a[i][1];
    f[i][1][1] = -a[i][1];
  }
//动态规划
  for (int j = 2; j <= m; j++)
    for (int i = 1; i <= n; i++) {
      for (int k = i - 1; k <= i + 1; k++) {
        if (k < 1 || k > n) continue;
        f[i][j][0] = max(f[i][j][0], f[k][j-1][0] + a[i][j]);
        f[i][j][1] = max(f[i][j][1], f[k][j-1][0] - a[i][j]);
        f[i][j][1] = max(f[i][j][1], f[k][j-1][1] + a[i][j]);
      }
    }

  int ans = -inf;
  for (int i = 1; i <= n; i++) {
    ans = max(ans, f[i][m][0]);
    ans = max(ans, f[i][m][1]);
  }
  
  printf("%d\n", ans);
  return 0;
}
