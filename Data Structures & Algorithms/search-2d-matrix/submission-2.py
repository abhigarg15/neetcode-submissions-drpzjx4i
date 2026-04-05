class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n*m-1


        while low <= high:
            mid = low + (high - low)//2

            newR = mid//m
            newC = mid%m

            if matrix[newR][newC] == target:
                return True
            elif matrix[newR][newC] < target:
                low = mid+1
            else:
                high = mid-1

        return False