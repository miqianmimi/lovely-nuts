#include <cstdio>
#include <cstring>

using namespace std;

const int inf = 1<<30;
const int maxn = 1000;
char s[maxn], t[maxn]; //s是第一个字符串，t是第二个
int n, m;  //其中n是第一个字符串的长度,m是第二个
int ans = inf; //全局变量

void calculate(int site){ //site是头的位置of那个第一个字符串的第一个数
	int i = 0, j = site;
	for (; i < n && j < m;){
		if (s[i] == t[j]){
			j++;
			i++;
		}
		else{
			j++;
		}
	}
	if (i == n){
		if (ans > j - site - n){ //ans 是全局变量
			ans = j - site - n;
		} //求最小值
	}
}
	

int main() {
	fgets(s, maxn, stdin);
	n = strlen(s);	
	fgets(t, maxn, stdin);
	m = strlen(t);
	s[--n] = '\0';
	t[--m] = '\0';
	printf("%d\n", m);
	printf("%d\n", n);


	for (int j = 0; j < m; j++){
		calculate(j);
	}
	if (ans == inf) {
    	puts(0);
    } 
	else {
    	printf("%d\n", 100 - ans);
    }
    return 0;
}

