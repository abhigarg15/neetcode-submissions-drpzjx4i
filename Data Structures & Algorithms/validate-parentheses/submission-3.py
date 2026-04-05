class Solution:
    def isValid(self, s: str) -> bool:
        #how to create a stack in python

        stack = []

        if len(s)%2 != 0:
            return False

        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            elif stack and i == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and i == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        
        return False
                