# 35. Search Insert Position
### Question:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

### Example:
Input: [1,3,5,6], 5
Output: 2

### Answer:
```
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if nums[0]>target:
                return 0
            elif nums[-1]<target:
                return(len(nums))
            else:
                for i in range(len(nums)):
                    if nums[i]<target and nums[i+1]>target:
                        return i+1
```

### Analysis:
唯一的难点在于，当算法官问到如何减少用时，可以用二分搜索的办法，降低算法时间复杂度。

### 题目分类:
* 二分搜索O(Log N)
