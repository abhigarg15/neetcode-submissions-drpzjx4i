class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        Method 1: we can do it O(n) time, but that would require space complexity of O(n)
        since we sould be using a dictionary, which will require O(n) space

        Method 2: we can do it in O(nlogn) time, by sorting the list, this way we dont need
        declare any additional space, hence saving on the space

        """

        # mp = Counter(nums)

        # for key,val in mp.items():
        #     if val > 1:
        #         return True
        # return False
        
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True

        # return False

        # this method is O(nlog(n))
        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True

        # return False

        # mp = Counter(nums)

        # for key, value in mp.items():
        #     if value > 1:
        #         return True

        # return False

        # mp = {}
        # for i in nums:
        #     if i in mp:
        #         return True
        #     else:
        #         mp[i] = 1

        # return False

        # s = set()
        # for num in nums:
        #     if num in s:
        #         return True
        #     else:
        #         s.add(num)

        # return False


        mp = Counter(nums)

        for num in nums:
            if mp[num] > 1:
                return True

        return False

    