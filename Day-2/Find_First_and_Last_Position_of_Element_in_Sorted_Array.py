class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Time complexity - O(Log(N))
        Space complexity - O(1)
        
        """
        if not nums:
            return [-1, -1]

        def find_left_index(i,j):
            left = -1
            
            while i<=j:
                mid = (i+j)//2
                if nums[mid] == target:
                    j = mid-1
                    left = mid
                elif nums[mid] > target:
                    j = mid-1
                else:
                    i = mid+1
            return left
        
        def find_right_index(i,j):
            right = -1
            
            while i<=j:
                mid = (i+j)//2
                if nums[mid] == target:
                    i = mid+1
                    right = mid
                elif nums[mid] > target:
                    j = mid-1
                else:
                    i = mid+1
            return right
        
        # First find left index
        left  = find_left_index(0, len(nums)-1)
        
        # Use left index as low to find right index
        right = find_right_index(left, len(nums)-1)
        return [left, right]          
                
