class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Standard binary search but on a specific range [l, h]
        def binary_search(l, h, target):
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            return -1

        n = len(nums)
        low, high = 0, n - 1
        pivot = 0 # Default if no rotation found

        # 1. Find the pivot (the smallest element's index)
        if nums[low] > nums[high]:
            while low <= high:
                mid = (low + high) // 2
                if mid < n - 1 and nums[mid] > nums[mid + 1]:
                    pivot = mid + 1
                    break
                if nums[mid] >= nums[0]:
                    low = mid + 1
                else:
                    high = mid - 1

        # 2. Decide which side to binary search
        # If target is between pivot and the end of the array
        if target >= nums[pivot] and target <= nums[n-1]:
            return binary_search(pivot, n - 1, target)
        # Otherwise search the left side
        else:
            return binary_search(0, pivot - 1, target)