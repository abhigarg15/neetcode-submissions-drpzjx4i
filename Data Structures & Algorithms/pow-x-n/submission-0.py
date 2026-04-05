class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x

            res = rec(x*x, n//2)
            return res if n%2 == 0 else res*x

        res = rec(x,abs(n))
        return res if n>=0 else 1/res 