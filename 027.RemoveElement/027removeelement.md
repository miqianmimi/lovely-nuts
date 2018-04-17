# 027. Remove Element
### Question:
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### Example:
```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
```

### Analysis:
先排序数组，使用两个指针，从头开始，碰到val的值，一个指针往前移，另一个不变。

### Solution in python:
```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=0
        nums.sort()
        while i<len(nums):
            if nums[i]!=val:
                nums[j]=nums[i]
                j=j+1
                i=i+1
            else:
                i=i+1
                j=j
        nums=nums[:j]
        print(nums)
        return len(nums)
```  

### Solution in C++:
```
class Solution {
public:
    int removeElement(vector<int>& nums, int val)
    {
        int cnt = 0;
        for(int i = 0 ; i < nums.size() ; ++i) 
        {
            if(nums[i] == val)
            {
                cnt++;
            }
            else
            {   
                nums[i-cnt] = nums[i];
            }
        }
        return nums.size()-cnt;
    };
};
```


### 本题关键：用两个指针遍历来取代O(N)空闲复杂度。
            
            
