class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = m*n-1
        
        while i <= j:
            
            mid = (i + j)//2
            
            # since matrix is stored as a large array we 
            # can use this to find row and column index
            
            mid_element = matrix[mid // n][mid % n]
            
            if mid_element == target:
                return True
            elif mid_element > target:
                j = mid-1
            else:
                i = mid+1
        
        return False
    
        #Time complexity - O(Log(m*n)) [standard binary search]
        #Space complexity - O(1)