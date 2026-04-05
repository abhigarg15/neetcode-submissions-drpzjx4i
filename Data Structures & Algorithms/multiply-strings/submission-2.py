class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def stringToint(s):
            n = len(s)
            res = 0
            for i in range(n):
                res = 10*res + int(s[i])

            return res
        print(stringToint(num1))
        print(stringToint(num2))    
        return str(stringToint(num1)*stringToint(num2))