class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        path = []

        def dfs(start):
            # record current subset
            res.append(path.copy())

            for i in range(start, len(nums)):
                # skip duplicates at the same depth
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res