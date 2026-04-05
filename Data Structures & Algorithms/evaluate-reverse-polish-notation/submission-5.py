class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val1 = 0

        for i in tokens:

            if i == "+" or i == "-" or i == "*" or i == "/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if i == "+":
                    val1 = val1 + val2
                elif i == "-":
                    val1 = val1 - val2
                elif i == "*":
                    val1 = val1 * val2
                elif i == "/":
                    val1 = val1 / val2
                stack.append(val1)
                print(val1)
            else:
                stack.append(i)
            
            # print(val1)


        return int(stack.pop())