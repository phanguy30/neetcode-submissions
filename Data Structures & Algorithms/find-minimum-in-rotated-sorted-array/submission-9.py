class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        pivot = 0 

        if nums[low] > nums[high]:
            while low <= high:
                mid = (low + high) // 2
                
                # Check if mid is the peak
                if mid < n - 1 and nums[mid] > nums[mid + 1]:
                    return nums[mid + 1] # Found it! Return immediately.
                
                # Standard binary search direction logic
                if nums[mid] >= nums[0]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return nums[pivot]