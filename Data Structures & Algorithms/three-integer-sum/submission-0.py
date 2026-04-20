class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        def backtrack(start, path):
            if len(path) == 3:
                if sum(path) == 0:
                    res.add(tuple(sorted(path)))  # tuple is hashable
                return

            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return [list(t) for t in res]