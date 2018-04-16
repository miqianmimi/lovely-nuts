# 16. 3Sum Closest
### Question:
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

### Example:
```
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
### Analysis:
所以我们需要定义一个变量diff用来记录差的绝对值，然后我们还是要先将数组排个序，
然后开始遍历数组，思路跟那道三数之和很相似，都是先确定一个数，
然后用两个指针left和right来滑动寻找另外两个数，每确定两个数，我们求出此三数之和，
然后算和给定值的差的绝对值存在newDiff中，然后和diff比较并更新diff和结果closest即可.

### 方法1：超时的最简单的遍历方法 O(n^3)复杂度
```
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        diff=target-nums[0]-nums[1]-nums[2]
        for xu,i in enumerate(nums):
            newtarget=target-i
            newnums=nums[xu+1:]
            for k,m in enumerate(newnums):
                for n in newnums[k+1:]:
                    if abs(diff)>abs(newtarget-m-n):
                        diff=newtarget-m-n
        tpp=target-diff
        return (tpp)
 ```
 
 ### 方法2： O(N^2)复杂度的做法
 ```
 class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
```
方法2 O(N^2)复杂度的做法同样是确定一个，然后确定另两个，但确定另两个的时候，当和<target，做指针从头往后移动，当和>target,右指针从右往左移动。

### 本题分类： 左右指针化简复杂度
