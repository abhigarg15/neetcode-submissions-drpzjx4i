class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def rec(start, curr):
  
            output.append(curr[::])
                
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                rec(i+1,curr)
                curr.pop()
 

        output = []
        rec(0,[])
        return output