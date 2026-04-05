class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for i in range(32):
            bit = (n>>i) & 1 # we check whether the bit is 0 or 1
            res |= bit << (31-i)

        return res