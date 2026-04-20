class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        path = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                # skip duplicates *at the same depth*
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                

                path.append(candidates[i])
                dfs(i + 1, remain - candidates[i])
                path.pop()

        dfs(0, target)
        return res