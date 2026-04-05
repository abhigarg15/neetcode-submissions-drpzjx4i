class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        leftCol = 0
        upRow = 0
        rightCol = COLS
        lowRow = ROWS
        
        ans = []

        while leftCol < rightCol and upRow < lowRow:  
            
            for i in range(leftCol,rightCol):
                ans.append(matrix[upRow][i])
            
            upRow+=1
            
            for i in range(upRow,lowRow):
                ans.append(matrix[i][rightCol-1])
            
            rightCol-=1

            if not (leftCol < rightCol and upRow < lowRow):
                break

            for i in range(rightCol-1, leftCol-1, -1):
                ans.append(matrix[lowRow-1][i])
            
            lowRow-=1

            for i in range(lowRow-1,upRow-1,-1):
                ans.append(matrix[i][leftCol])
            
            leftCol+=1


        return ans