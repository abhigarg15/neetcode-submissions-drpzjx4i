class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod, zero_cnt = 1, 0
        # for num in nums:
        #     if num != 0:
        #         prod *= num # I am multiplying only when we are non zero
        #     else:
        #         zero_cnt += 1

        # if zero_cnt > 1: return [0]* len(nums) # Everything is 0 then

        # res = [0]* len(nums)

        # for i, c in enumerate(nums):
        #     if zero_cnt > 0 :
        #         if c != 0:
        #             res[i] = 0
        #         else:
        #             res[i] = prod
        #     else:
        #         res[i] = prod // c
        # return res        

        """
        Understand we would need a product any way, what complicates the method is the use
        of zero
        """

        # prod = 1
        # zero_cnt = 0
        # for num in nums:
        #     if num != 0:
        #         prod*=num
        #     else:
        #         zero_cnt += 1
        
        # if zero_cnt > 1:
        #     return [0]*len(nums)

        # res = [0] *len(nums)

        # for i,n in enumerate(nums):
        #     if zero_cnt > 0:
        #         if n != 0:
        #             res[i]=0
        #         else:
        #             res[i] = prod

        #     else:
        #         res[i] = prod//n


        # return res


        prod = 1
        Zeros = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0:
                Zeros += 1
            else:
                prod *= nums[i]

        print(prod)

        if Zeros > 1:
            return [0 for _ in range(len(nums))]

        elif Zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans.append(prod)
                else:
                    ans.append(0)

        else:
            for i in range(len(nums)):
                ans.append(prod//nums[i])

        return ans
            










