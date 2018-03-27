class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        C = 1
        count = 0
        for i in nums:
            if i == 0:
                count = count + 1
            C = C * i
        if C != 0:
            for i, j in enumerate(nums):
                nums[i] = C / j
        elif C == 0 and count == 1:
            m = []
            for i, j in enumerate(nums):
                if j != 0:
                    m.append(0)
                    continue
                elif j == 0:
                    D = 1
                    for P in nums:
                        if P != 0:
                            D = D * P
                    m.append(D)
                    print(i)
                    print(D)
            nums = m
        elif C == 0 and count >= 2:
            m = []
            for i, j in enumerate(nums):
                m.append(0)
            nums = m

        return (nums)
class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf2(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


