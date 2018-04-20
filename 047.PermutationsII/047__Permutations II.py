class Solution(object):
    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range((p + [n]).index(n) + 1)]
        return perms


class Solution2(object):
    def permuteUnique(self, nums):
        if not nums:
            return []
        nums = sorted(nums)
        res = []
        path = []
        self.dfs(nums, path, res)
        return res

    def dfs(self, s, path, res):
        if not s:  # 如果用完了
            res.append(path)
            return
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            self.dfs(s[:i] + s[i + 1:], path + [s[i]], res)
