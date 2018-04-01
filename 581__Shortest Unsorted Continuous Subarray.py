class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        for i in nums:
            a.append(i)
        a.sort()
        print(a)
        c = 0
        d = 0
        for p, i in enumerate(a):
            if i != nums[p]:
                c = p
                break
                print(c)

        for p in range(len(nums) - 1, 0, -1):
            if a[p] != nums[p]:
                d = p
                break
                print(d)
        print(d, c)
        if d == c:
            return (0)
        return (d - c + 1)

