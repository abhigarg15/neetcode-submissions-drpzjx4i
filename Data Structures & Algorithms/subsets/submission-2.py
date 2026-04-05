class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def rec(idx, curr):
            output.append(curr[:])

            if len(curr) == len(nums):
                return

            for i in range(idx,len(nums)):
                curr.append(nums[i])
                rec(i+1,curr)
                curr.pop()

        rec(0,[])

        return output