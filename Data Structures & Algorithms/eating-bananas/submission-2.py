class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # minimize k

        high = max(piles)
        low = 1
        res = low
        while low <= high:
            mid = (low + high) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/mid)
            if totalTime <= h:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res