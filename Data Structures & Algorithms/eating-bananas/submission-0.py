import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def get_time(k):
            total_hours = 0
            for pile in piles:
                # Round up division: e.g., 7 bananas at 3/hr = 3 hours
                total_hours += math.ceil(pile / k)
            return total_hours

        low = 1
        high = max(piles)
        res = high # Default to the max speed

        while low <= high:
            mid = (low + high) // 2
            
            # If Koko can finish within h hours at speed 'mid'
            if get_time(mid) <= h:
                res = mid      # This speed works, but can we go slower?
                high = mid - 1
            else:
                # Too slow! Need to increase speed
                low = mid + 1
                
        return res