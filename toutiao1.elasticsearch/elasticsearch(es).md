# Elastic Search(ES)

### Question:
ES有一个经典的问题，计算一个query与文档的匹配度，简化描述如下：
ES会对用户query进行切词操作，query被切割成多个关键字a,b,c;
然后ES会在倒排索引中寻找a/b/c并且回溯关键字在文档的位置，从而计算匹配度，现在模拟ES计算query匹配度的方法，给出如下问题的解。

### Exampe:
```
输入“mbh"切词后，分别为”m","b","h"(模拟切词后的3个关键字)，“amhbgyhdc"（模拟一个ES的一个文档）
关键字m出现在第2个位置，
关键字b出现在第4个位置，
关键字h出现在第3，7个位置，
但第3个位置与QUERY关键字逆序，为简化流程，可以排除掉；
如果没有匹配到所有关键字，打分为0分；
如果匹配到所有关键字，打分为100分，但要区分出相似程度；
m-b 隔了一个词，100-1=99
b-n 隔了两个词，99-1=98；
最后这个例子的匹配度为98分。

输入：
mbh
amhbghdc

输出：
98
```

### Analysis:
等价描述，换一个方法描述题目，就能做出来，做法就显示出来。
串和序列。串指连续的，序列是跳着选的。
给两个字符串，找一个字符串在另一个字符串的序列位置，子序列形式，使得序列尾-头最小。
1.扫一遍，确定是不是一个字符串在另一个字符串中？0，1
2.【1，3，5】头如果固定了，尾巴越往前越好。每个越往前取越好。贪心算法。
首字符位置确定了，以找最近的字符的位置的长度，找到了，就记录一个当前首字符位置的最短长度。
然后把所有首字符的位置都确定一遍，然后记录所有的最短长度。得到最小的就OK。

* 1<<30,左移一位相当于乘以2，左移30位应该是相当于乘以2的30次 ...

### Solution:C++
```c
#include <cstdio>
#include <cstring>

using namespace std;

const int inf = 1<<30;
const int maxn = 1000;
char s[maxn], t[maxn]; //s是第一个字符串，t是第二个
int n, m;  //其中n是第一个字符串的长度,m是第二个
int ans = 0; //全局变量

void calculate(int site){ //site是头的位置of那个第一个字符串的第一个数
	int i = 0, j = site;
	for (; i < n && j < m;){
		if (s[i] == t[j]){
			j++
			i++
		}
		else{
			j++
		}
	}
	if (i == n){
		if (ans > j - site - n){ //ans 是全局变量
			ans = j - site - n
		} //求最小值
	}
}
	

int main() {
	fgets(s, maxn, stdin);
	n = strlen(s);	
	fgets(t, maxn, stdin);
	m = strlen(t);

  for (int j = 0; j < m; j++)
      calculate(j);
  if (ans == inf) {
    printf(0);
  } 
  else {
    printf("%d\n", 100 - ans);
  }
  return 0;
}




```

