class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first transpose and than reverse every row, for clockwise rotations

        ROWS = len(matrix)
        COLS = len(matrix[0])
        for i in range(ROWS):
            for j in range(i,COLS):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        for row in matrix:
            row.reverse()

        