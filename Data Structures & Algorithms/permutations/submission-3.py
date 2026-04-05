import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Shortcut solution
        """
        # return [list(permute) for permute in list(itertools.permutations(nums))]
       
        # def rec(curr):
        #     if len(curr) == len(nums):
        #         output.append(curr[:])
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] not in curr:
        #             curr.append(nums[i])
        #             rec(curr)
        #             curr.pop()


        # output = []
        # rec([])
        # return output

        # output = []

        # def rec(curr):
        #     if len(curr) == len(nums):
        #         output.append(curr[:])
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] not in curr:
        #             curr.append(nums[i])
        #             rec(curr)
        #             curr.pop()
            
        # rec([])

        # return output
        output = []
        def rec(curr):
            if len(curr) == len(nums):
                output.append(curr[:])
                return


            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    rec(curr)
                    curr.pop()


        rec([])

        return output
            

