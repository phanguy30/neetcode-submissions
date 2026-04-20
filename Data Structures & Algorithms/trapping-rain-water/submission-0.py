from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        water = 0

        while l < n:
            # 1) find left wall
            while l < n and height[l] == 0:
                l += 1
            if l >= n:
                break

            # 2) find first r >= left wall
            r = l + 1
            best = -1  # index of tallest bar seen to the right (fallback)
            while r < n and height[r] < height[l]:
                if best == -1 or height[r] >= height[best]:
                    best = r
                r += 1

            # if we ran off the end, no bar >= height[l] exists
            if r == n:
                if best == -1:
                    break  # nothing to the right at all
                r = best

            # 3) fill between l and r
            bound = min(height[l], height[r])
            for i in range(l + 1, r):
                if height[i] < bound:
                    water += bound - height[i]

            # 4) advance
            l = r

        return water