class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        print(slow, fast)
        return fast