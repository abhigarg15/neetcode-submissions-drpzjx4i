class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        TC = O(n)
        SC = O(n)
        """
        # left = []
        # star = []
        # for i,ch in enumerate(s):
        #     if ch == "(":
        #         left.append(i)
        #     elif ch == "*":
        #         star.append(i)
        #     else:
        #         if not left and not star:
        #             return False # we have encountered ")" or "*" and the stacks are empty
        #         if left:
        #             left.pop()
        #         else:
        #             star.pop()

        # while left and star:
        #     if left.pop() > star.pop():
        #         return False
        
        # return not left

        """
        Tyring recursion
        """
        # def dfs(i,open):
        #     if open < 0:
        #         return False
        #     if i == len(s):
        #         return open == 0

        #     if s[i] == "(":
        #         return dfs(i+1, open+1)
        #     elif s[i] == ")":
        #         return dfs(i+1, open-1)
        #     else:
        #         return dfs(i+1,open) or dfs(i+1,open+1) or dfs(i+1,open-1)

        # return dfs(0,0)

        """
        Greedy Algorithm
        """
        leftmin = 0
        leftmax = 0

        for c in s:
            if c == "(":
                leftmin += 1
                leftmax += 1
            elif c == ")":
                leftmin -= 1
                leftmax -= 1
            else: # we encountered a star
                leftmin -= 1
                leftmax += 1
            if leftmax < 0: 
                return False
            if leftmin < 0:
                leftmin = 0

        return leftmin == 0
                

