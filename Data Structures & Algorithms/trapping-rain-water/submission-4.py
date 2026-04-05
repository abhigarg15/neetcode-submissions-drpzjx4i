class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        n = len(height)
        
        leftMax = [0]*n
        rightMax = [0]*n

        #check from the right to left
        #
        resR = 0
        for i in range(n-1, -1, -1):
            resR = max(height[i],resR)
            rightMax[i] = resR

        resL = 0
        for i in range(0, n):
            resL = max(height[i],resL)
            leftMax[i] = resL

        totalWater = 0

        for i in range(n):
            totalWater += min(leftMax[i],rightMax[i]) - height[i]

        return totalWater
