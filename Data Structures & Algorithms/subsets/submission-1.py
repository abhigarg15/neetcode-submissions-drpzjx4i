class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # def rec(start,curr):
        #     output.append(curr[:])

        #     if len(curr) == len(nums):
        #         return
            
        #     for i in range(start,len(nums)):
        #         curr.append(nums[i])
        #         rec(i+1,curr)
        #         curr.pop()



        # output = []
        # rec(0,[])
        # return output

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