class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack = []

        # res = []

        # def backtrack (openN, closedN):

        #     if openN == closedN == n:
        #         print(stack)
        #         res.append("".join(stack))
        #         return
            
        #     if openN < n:
        #         stack.append("(")
        #         backtrack(openN+1, closedN)
        #         stack.pop()

        #     if closedN < openN:
        #         stack.append(")")
        #         backtrack(openN, closedN+1)
        #         stack.pop()



        # backtrack(0,0)
        # return res

        ans = []
        def rec(s, openB, closeB):
            if len(s) == 2*n:
                ans.append("".join(s))
                return

            if openB < n:
                s.append("(")
                rec(s, openB+1,closeB)
                s.pop()
            
            if closeB < openB:
                s.append(")")
                rec(s, openB, closeB+1)
                s.pop()
            

        rec([],0, 0)

        return ans