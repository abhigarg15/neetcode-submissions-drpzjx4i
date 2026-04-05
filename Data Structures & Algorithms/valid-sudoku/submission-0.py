class Solution:
    # def smallbox(self,i:int, j:int) ->bool:



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            m = {}
            for j in range(0,len(board[i])):
                if board[i][j] == ".":
                    continue
               
                if board[i][j] not in m:
                    m[board[i][j]] = 1
                else:
                    print(i,j)
                    print(board[i][j])
                    return False

        for i in range(0,len(board)):
            m = {}
            for j in range(0,len(board[i])):
                if board[j][i] == ".":
                    continue
    
                if board[j][i] not in m:
                    m[board[j][i]] = 1
                else:
                    print(i,j)
                    print(board[i][j])
                    return False

        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                m = {}
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        if board[a][b] == ".":
                            continue
                        if board[a][b] not in m:
                            m[board[a][b]] = 1
                        else:
                            return False    

        return True