class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #obviously we need to sort the array, other wise it becomes impossible to find the combination,
        # it will go to O(n^3) complexity

        '''
        if not sorting than below is the solution
        '''
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range( j+1 , len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
                    
        #                 res.add(tuple([nums[i],nums[j],nums[k]]))

        
        # return [list(i) for i in res]

        res = []
        nums.sort()

        for i,a in enumerate(nums):
            
            if i and a == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l < r:

                val = a + nums[l] + nums[r]

                if val > 0:
                    r -= 1
                elif val < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    # r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res 


        



        