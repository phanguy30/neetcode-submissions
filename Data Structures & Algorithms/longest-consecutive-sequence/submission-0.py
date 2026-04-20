class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            if curr-1 not in store:
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res