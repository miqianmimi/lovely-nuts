#include <cstdio>
#include <cstring>

using namespace std;

const int inf = ~0u>>1;
const int maxn = 1002;
char s[maxn], t[maxn];
int n, m;
int ans = inf;

void work(int st) {
  int j = 0, i = st;
  for (; i < m && j < n; i++) {
    if (s[j] == t[i]) {
      j++;
    }
  }
  if (j == n) {
    if (ans > i - st - n)
      ans = i - st - n;
  }
}

int main() {
  fgets(s, maxn, stdin);
  n = strlen(s);
  s[--n] = '\0';
  fgets(t, maxn, stdin);
  m = strlen(t);
  t[--m] = '\0';
  
  for (int i = 0; i < m; i++)
    if (t[i] == s[0])
      work(i);
  if (ans == inf) {
    puts("0");
  } else {
    printf("%d\n", 100 - ans);
  }
  return 0;
}
