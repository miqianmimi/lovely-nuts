# 40 . Combination Sum II

### Question:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

### Example:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

### Analysis:
Backtracking= DFS
[深度优先算法的介绍](https://blog.csdn.net/raphealguo/article/details/7560918)
```
/** 
 * DFS核心伪代码 
 * 前置条件是visit数组全部设置成false 
 * @param n 当前开始搜索的节点 
 * @param d 当前到达的深度 
 * @return 是否有解 
 */  
bool DFS(Node n, int d){  
    if (isEnd(n, d)){//一旦搜索深度到达一个结束状态，就返回true  
        return true;  
    }  
  
    for (Node nextNode in n){//遍历n相邻的节点nextNode  
        if (!visit[nextNode]){//  
            visit[nextNode] = true;//在下一步搜索中，nextNode不能再次出现  
            if (DFS(nextNode, d+1)){//如果搜索出有解  
                //做些其他事情，例如记录结果深度等  
                return true;  
            }  
  
            //重新设置成false，因为它有可能出现在下一次搜索的别的路径中  
            visit[nextNode] = false;  
        }  
    }  
    return false;//本次搜索无解  
}  
```
这道题和 Combination Sum 极其相似，主要的区别是Combination Sum中的元素是没有重复的，且每个元素可以使用无限次；而这题中的元素是有重复的，每个元素最多只能使用一次。最开始的想法是加下一个元素时不要考虑当前元素，且把结果用集合存储以防止重复的组合出现，但结果超时了。改用手动把所有与当前元素相等的元素都去掉即可。



### Solution:
```
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        li=[]
        visit=[]
        candidates.sort()
        if target==0:
            return li
        if not candidates:
            return li
        
        self.dfs(candidates,target,visit,li)
        return li
        
        
    def dfs(self,candidates,target,visit,li):
        s =sum(visit) if visit else 0
        if s>target:
            return
        elif s==target:
            li.append(visit)
            return
        else:
            i = 0
            while i < len(candidates):
                self.dfs(candidates[i + 1:], target, visit + [candidates[i]], li)
                # ignore repeating elements
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1
```

# 本题关键：
* 用到回溯算法和DFS深度优先
* `很重要的题目`
* ***需要复习的题***                       
                        
