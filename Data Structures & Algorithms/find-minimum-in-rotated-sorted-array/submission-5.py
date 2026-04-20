class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        # If the array isn't rotated at all, return the first element
        if nums[low] <= nums[high]:
            return nums[low]

        while low <= high:
            mid = (low + high) // 2

            # 1. FOUND THE BREAK POINT (Case A)
            # If the current element is smaller than the one before it, 
            # 'mid' is the minimum.
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # 2. FOUND THE BREAK POINT (Case B)
            # If the current element is greater than the one after it, 
            # 'mid + 1' is the minimum.
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # 3. DECIDE DIRECTION
            # If middle is greater than high, the break point is to the right
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the break point is to the left
            else:
                high = mid - 1
                
        return nums[low]