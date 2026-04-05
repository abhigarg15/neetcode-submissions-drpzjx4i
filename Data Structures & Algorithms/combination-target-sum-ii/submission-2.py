class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def rec(start, curr):
            if sum(curr) == target:
                output.append(curr[:])
                return
            if sum(curr) > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                rec(i+1,curr)
                curr.pop()



        output = []
        rec(0,[])
        return output

