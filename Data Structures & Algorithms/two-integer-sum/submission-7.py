class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TC = O(n)
        SC = O(n)
        """
        # tracker = {}

        # for i in range(len(nums)):
        #     if target - nums[i] in tracker:
        #         # ans = []
        #         # ans.extend([tracker[target - nums[i]],i])
        #         return [tracker[target - nums[i]],i]
        #     else:
        #         tracker[nums[i]] = i

        # return []


        # TC = O(n)
        # SC = O(n)
        # mp = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in mp:
        #         return [mp[target - nums[i]],i]
        #     else:
        #         mp[nums[i]] = i

        # return []

        mp = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in mp:
                ans.extend([mp[target - nums[i]], i])
            else:
                mp[nums[i]] = i


        return ans
