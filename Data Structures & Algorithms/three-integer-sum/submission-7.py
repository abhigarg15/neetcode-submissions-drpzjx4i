class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # res = []
        # nums.sort()

        # for i,a in enumerate(nums):
            
        #     if i and a == nums[i-1]:
        #         continue

        #     l = i+1
        #     r = len(nums)-1

        #     while l < r:
        #         val = a + nums[l] + nums[r]

        #         if val > 0:
        #             r-=1
        #         elif val < 0:
        #             l+=1
        #         else:
        #             res.append([a,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l] == nums[l-1] and l < r:
        #                 l+=1
        # return res


        res = []
        i = 0
        nums.sort() # only achievable if we sort (O(n).log(n))
        while i < len(nums)-2:
        
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
                
            j = i+1 # second ele

            k = len(nums)-1 # third ele

            while j < k:
                tmp = nums[i] + nums[j] + nums[k]

                if tmp == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1

                    while k > j and nums[k] == nums[k+1]:
                        k-=1
                elif tmp < 0:
                    j+=1
                else:
                    k-=1

            i+=1


        
        return res








                