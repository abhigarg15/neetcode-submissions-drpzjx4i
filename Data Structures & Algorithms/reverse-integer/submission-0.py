class Solution:
    def reverse(self, x: int) -> int:
        
        # res = 0
        # for i in range(31):
        #     bit = (x>>i) & 1 # if it is 1 than we recreate the number
        #     res |= bit << (30-i)

        # return res

        tmp = str(abs(x))[::-1]
        if -2**31 <= int(tmp) <= 2**31-1:
            if x < 0:
                return -1*int(tmp)
            else:
                return int(tmp)
        
        return 0
        # if -2**31 <= int(tmp) <= 2**31 -1:
        #     if x < 0:
        #         return -1*int(tmp)
        #     else:
        #         return int(tmp)
        
        return 0