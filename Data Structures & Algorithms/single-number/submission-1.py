class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ans = 0
        # for num in nums:
        #     ans ^= num

        # return ans
        hset = set()
        for num in nums:
            if num in hset:
                hset.remove(num)
            else:
                hset.add(num)
        
        return list(hset)[0]