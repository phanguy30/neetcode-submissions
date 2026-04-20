class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Start with the first number so we can handle all-negative arrays
        max_res = nums[0]
        current_sum = 0
        
        for num in nums:
            # If our current_sum is negative, it's a "burden"—throw it away
            if current_sum < 0:
                current_sum = 0
            
            current_sum += num
            max_res = max(max_res, current_sum)
            
        return max_res