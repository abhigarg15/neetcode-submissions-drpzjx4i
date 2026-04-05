import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(permute) for permute in list(itertools.permutations(nums))]
       