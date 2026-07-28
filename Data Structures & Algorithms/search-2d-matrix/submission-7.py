class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# Brute force this by searching each row one by one to see if the idx matches the target. This leads to a complexity
# of O(n*m) since we iterate through the whole m rows and n columns. We can use binary search to find the exact row 
# and then perform binary search again to find the column 
        def find_row(matrix,target):
            n = len(matrix)
            l,r = 0, n-1
            while l<=r:
                mid = (l+r)//2
                if matrix[mid][0]<=target<=matrix[mid][-1]:
                    return mid
                elif matrix[mid][0]<target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        row = find_row(matrix,target)
        if row == -1:
            return False
        l,r = 0, len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]> target:
                r = mid - 1
            elif matrix[row][mid]< target:
                l = mid + 1
            else: 
                return True
        return False

