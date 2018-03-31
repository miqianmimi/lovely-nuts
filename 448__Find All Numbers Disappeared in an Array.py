class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            print(index)#把出现过的数字的位置的数变成相反数
            nums[index] = - abs(nums[index])
        print(nums)
        #把那些仍为正的数的序号提起出来
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]