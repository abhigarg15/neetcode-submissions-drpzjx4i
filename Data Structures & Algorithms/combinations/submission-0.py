class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def rec(i,arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            
            for j in range(i,n+1):
                rec(j+1,arr + [j])
        
        rec(1,[])

        return ans