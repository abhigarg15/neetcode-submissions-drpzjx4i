class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        nums.sort()

        def rec(idx, curr,total):
            if total == target:
                res.append(curr[:])
                return 

            if total > target or idx >= len(nums):
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                if total + nums[i] > target:
                    break

                curr.append(nums[i])
                rec(i+1,curr, total + nums[i])
                curr.pop()


        rec(0,[],0)
        return res



