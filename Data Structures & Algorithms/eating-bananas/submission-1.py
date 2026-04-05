class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        ans = 0
        while low <= high:
            mid = low + (high - low)//2

            total_time = 0
            
            for pile in piles:
                total_time += math.ceil(float(pile)/mid)
            
            if total_time <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans