class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes algorithm
        # ans = nums[0]
        # currSum = 0
        # for i in range(len(nums)):
        #     if currSum < 0:
        #         currSum = 0
        #     currSum += nums[i]
        #     ans = max(ans, currSum)

        # return ans
        """
        Recursion Method
        """

        # csum = 0
        # ans = nums[0]
        # for num in nums:
        #     if csum < 0:
        #         csum = 0
        #     csum += num

        #     ans = max(csum,ans)
        
        # return ans

        csum = 0
        res = float("-inf")
        for num in nums:
            csum += num
            res = max(res,csum)
            if csum < 0:
                csum = 0
        
        return res