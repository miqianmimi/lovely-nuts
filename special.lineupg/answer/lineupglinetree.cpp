#include <algorithm>
#include <cstdio>
#include <cstring>
#include <thread>
#include <vector>
const int inf = ~0u>>1;
const int maxn = 100000;
const int maxq = 180000;
const int max_thread = 4;
struct Node {
  Node() : min(inf), max(0) {}
  void Update(int v) {
    if (min > v) min = v;
    if (max < v) max = v;
  }
  void Update(const Node &n) {
    if (min > n.min) min = n.min;
    if (max < n.max) max = n.max;
  }
  int min, max;
} node[maxn * 2 + 1];
int n, q;
int h[maxn];
int qx[maxq], qy[maxq];
int res[maxq];
std::vector<std::thread*> threads;
int GetInt() {
  char ch;
  while (ch = getchar(), !('0' <= ch && ch <= '9'));
  int ret = ch - 48;
  while (ch = getchar(), '0' <= ch && ch <= '9') ret = ret * 10 + ch - 48;
  return ret;
}
inline int get_id(int l, int r) {
  return (l + r) | (l != r);
}
void Insert(int l, int r, int s, int v) {
  if (l <= s && s <= r) {
    node[get_id(l, r)].Update(v);
    if (l < r) {
      int mid = (l + r) >> 1;
      Insert(l, mid, s, v);
      Insert(mid + 1, r, s, v);
    }
  }
}
Node GetMinMax(int l, int r, int s, int t) {
  if (s <= l && r <= t) {
    return node[get_id(l, r)];
  }
  Node ret;
  int mid = (l + r) >> 1;
  if (s <= mid) ret = GetMinMax(l, mid, s, t);
  if (mid + 1 <= t) ret.Update(GetMinMax(mid + 1, r, s, t));
  return ret;
} 
void Process(int l, int r) {
  Node ret;
  for (int i = l; i < r; i++) {
    ret = GetMinMax(1, n, qx[i], qy[i]);
    res[i] = ret.max - ret.min;
  }
}
int main() {
  freopen("lineupg.in", "r", stdin);
  freopen("lineupg.out", "w", stdout);
  scanf("%d%d\n", &n, &q);
  for (int i = 1; i <= n; i++) {
    h[i] = GetInt();
    Insert(1, n, i, h[i]);
  }
  Node ret;
  for (int i = 0; i < q; i++) {
    qx[i] = GetInt();
    qy[i] = GetInt();
  }
  int num_thread = 1;
  if (q > 1000)
    num_thread = max_thread;
  int query_per_thread = q / num_thread;
  for (int i = 0; i < num_thread; i++) {
    int l = i * query_per_thread;
    int r = (i + 1) * query_per_thread;
    if (i == num_thread - 1)
      r = q;
    auto th = new std::thread(Process, l, r);
    threads.push_back(th);
  }
  for (auto th : threads)
    th->join();
  for (int i = 0; i < q; i++)
    printf("%d\n", res[i]);
  for (auto th : threads)
    delete th;
  return 0;
}
