class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = []
        for i in range(n+1):
            tmp = i
            ans = 0
            while tmp:
                if tmp%2:
                    ans+=1

                tmp = tmp >> 1
            output.append(ans)
        return output 