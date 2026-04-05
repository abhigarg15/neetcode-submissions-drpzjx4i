class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TC = O(n)
        SC = O(n)
        """
        tracker = {}

        for i in range(len(nums)):
            if target - nums[i] in tracker:
                ans = []
                ans.extend([tracker[target - nums[i]],i])
                return ans;
            else:
                tracker[nums[i]] = i

        return []