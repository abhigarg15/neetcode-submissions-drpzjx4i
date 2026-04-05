class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        Method 1: we can do it O(n) time, but that would require space complexity of O(n)
        since we sould be using a dictionary, which will require O(n) space

        Method 2: we can do it in O(nlogn) time, by sorting the list, this way we dont need
        declare any additional space, hence saving on the space

        """

        # check = {}

        # for num in nums:
        #     if num in check:
        #         return True
        #     else:
        #         check[num] = check.get(num,0)+1
        
        # return False

        nums = sorted(nums)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        
        return False

        