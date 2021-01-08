class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        Time complexity - O(LogN)
        Space complexity - O(1)
        """
        def find_pivot(low, high):
            if nums[low] < nums[high]:
                return 0
            
            while low <= high:
                mid = (low + high)//2
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                else:
                    if nums[mid] >= nums[low]:
                        low = mid + 1
                    else:
                        high = mid - 1
        
        def search(low, high):
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        
        # Main logic
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        low = 0
        high = len(nums)-1
        
        # Search pivot first
        pivot = find_pivot(low, high)
        
        if nums[pivot] == target:
            return pivot
        
        # If pivot is 0 then we perform normal binary search
        if pivot == 0:
            return search(low, high)
        
        # If this condition is true then we know target lies between pivot and high
        if target < nums[0]:
            return search(pivot, high)
        
        return search(low, pivot)

class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        Time complexity - O(LogN)
        Space complexity - O(1)
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        
        return -1
