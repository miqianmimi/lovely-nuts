class Solution():
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        res = [[]]
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        for i in range(index, len(nums)):
            res.append(path + [nums[i]])
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res) #i 记录层， path记录走了哪些元素，res返回全部
            path.pop()


a=Solution()
b=a.subsets([1,3,2])
print(b)

    #用res代替return的好办法