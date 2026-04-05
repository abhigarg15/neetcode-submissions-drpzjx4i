class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def rec(start,curr):
            if sum(curr) == target:
                output.append(curr[:])
                return
            if sum(curr) > target:
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                rec(i, curr)
                curr.pop()

        output = []
        rec(0,[])
        return output

            