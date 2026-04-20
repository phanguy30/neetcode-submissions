class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        

        while low <= high: 
            half = (low+high)//2
            if target < nums[half]:
                high = half -1
            elif target > nums[half]:
                low = half+1

            else:
                return half
            
        return -1
        
        