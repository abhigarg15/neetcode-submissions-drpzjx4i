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

        nums = list(set(nums))
        nums.sort()
        print(nums)
        res = 1
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                tmp+=1
            else:
                tmp = 1

            res = max(tmp, res)

        return res



