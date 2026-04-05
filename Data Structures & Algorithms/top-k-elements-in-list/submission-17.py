class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        

        for key, val in count.items():
            freq[val].append(key)
        
        arr = []
        for i in range(len(freq)-1,0,-1):
            arr.extend(freq[i])

            if len(arr) == k:
                return arr
        
        return arr

