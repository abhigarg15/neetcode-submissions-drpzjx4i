class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    for a in range(COLS):
                        if matrix[i][a] == 0:
                            continue
                        matrix[i][a] = -1
  
                    for a in range(ROWS):
                        if matrix[a][j] == 0:
                            continue
                        matrix[a][j] = -1
      

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

                