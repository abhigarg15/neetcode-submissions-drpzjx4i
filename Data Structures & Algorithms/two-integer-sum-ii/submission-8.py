class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mp = defaultdict(int)
        # for i in range(len(numbers)):
        #     tmp = target - numbers[i]
        #     if mp[tmp]:
        #         return [mp[tmp], i + 1]
        #     mp[numbers[i]] = i + 1
        # return []

        #Two pointers

        # l = 0
        # r = len(numbers) -1 

        # while l < r:

        #     if numbers[l] + numbers[r] == target:
        #         return [ l+1, r+1]

        #     if numbers[l] + numbers[r] > target:
        #         r -= 1
        #     else:
        #         l += 1

        # return []


        #Binary Search
        # l = 0
        # r = len(numbers)-1
        # while l < r:
        #     val = numbers[l] + numbers[r]
        #     if val == target:
        #         return [l+1,r+1]

        #     elif val < target:
        #         l+=1
        #     else:
        #         r-=1


        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1

        return ans
            