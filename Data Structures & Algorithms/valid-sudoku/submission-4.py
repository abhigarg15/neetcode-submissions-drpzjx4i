class Solution:
    # def smallbox(self,i:int, j:int) ->bool:



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols = defaultdict(list)
        # rows = defaultdict(list)
        # squares = defaultdict(list)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
        #             return False
                
        #         cols[c].append(board[r][c])
        #         rows[r].append(board[r][c])
        #         squares[(r // 3, c // 3)].append(board[r][c])


        # return True

        # rows = defaultdict(list)
        # cols = defaultdict(list)
        # square = defaultdict(list)


        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
                
        #         if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
        #             return False


        #         rows[r].append(board[r][c])
        #         cols[c].append(board[r][c])
        #         square[(r//3,c//3)].append(board[r][c])

        # return True



        R = defaultdict(set) # keeping the track of all the elements in each row the length of R would be 9
        C = defaultdict(set)
        Box = defaultdict(set)
        
        def isValid(r:int , c:int)->bool:
            val = board[r][c]

            if val in R[r] or val in C[c] or val in Box[(r//3,c//3)]:
                return False

            R[r].add(val)
            C[c].add(val)
            Box[(r//3,c//3)].add(val)
            return True



        ROWS = len(board) # len of board
        COLS = len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                
                if not isValid(i,j):
                    return False

        return True



