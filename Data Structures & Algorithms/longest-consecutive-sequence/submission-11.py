class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 0:
        #     return 0
        # nums = set(nums)
        # ans = 1
        # for num in nums:
        #     if num - 1 not in nums:
        #         temp = 1
        #         while num+temp in nums:
        #             temp += 1
                
        #         ans = max(ans, temp)

        # return ans
        # if not nums:
        #     return 0

        # track = set(nums)
        # tmp = 0
        # res = 0
        # for i in nums:
        #     if i-1 not in track:
        #         tmp=1
            
        #     while i+tmp in track:
        #         tmp+=1

        #     res = max(res, tmp)
        # return res



        if not nums:
            return 0

        s = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                length=1
                while nums[i]+length in s:
                    length+=1

                res = max(res,length)

        return res


