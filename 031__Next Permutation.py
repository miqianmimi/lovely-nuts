class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       #弄一个指针来决定第一个换位置的点

        if len(nums) <= 1: return nums
        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break
        if partition == -1:
            nums.reverse()
            return nums
        else:
            for i in range(len(nums) - 1, partition, -1): #从最大的开始变小，交换两者的纸质
                print (nums[i],nums[partition])
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        nums[partition + 1:len(nums)] = nums[partition + 1:len(nums)][::-1]
        return nums

a=Solution()
b=a.nextPermutation([1,4,8,3,2])
print(b)

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       #弄一个指针来决定第一个换位置的点

        if len(nums) <= 1: nums=nums
        else:
            partition = -1
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    partition = i
                    break
            #print(partition)
            if partition == -1:
                nums.reverse()
            elif partition != -1:
                for i in range(len(nums) - 1, partition, -1): #从最大的开始变小，交换两者的纸质
                    if nums[i] > nums[partition]:
                        nums[i], nums[partition] = nums[partition], nums[i]
                        break
                nums[partition + 1:len(nums)] = nums[partition + 1:len(nums)][::-1]

