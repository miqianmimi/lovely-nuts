class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        li = []
        visit = []
        candidates.sort()
        if target == 0:
            return li
        if not candidates:
            return li

        self.dfs(candidates, target, visit, li)
        return li

    def dfs(self, candidates, target, visit, li):
        s = sum(visit) if visit else 0
        if s > target:
            return
        elif s == target:
            li.append(visit)
            return
        else:
            i = 0
            while i < len(candidates):
                self.dfs(candidates[i + 1:], target, visit + [candidates[i]], li)
                # ignore repeating elements
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1


