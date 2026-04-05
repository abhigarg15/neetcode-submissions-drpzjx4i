import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # self.nums = nums
        # self.k = k
        # heapq.heapify(self.nums)

        # if len(self.nums) > k:
        #     while len(self.nums) > k:
        #         heapq.heappop(self.nums)

        self.nums = nums
        self.k = k
        self.q = []
        for num in nums:
            if len(self.q) < self.k:
                heapq.heappush(self.q,num)
            else:
                heapq.heappushpop(self.q,num)
    
    def add(self, val: int) -> int:
        # if len(self.nums) < self.k:
        #     heapq.heappush(self.nums, val)
        # else:
        #     heapq.heappushpop(self.nums, val)

        # return self.nums[0]

        if len(self.q) < self.k:
            heapq.heappush(self.q,val)
        elif len(self.q) == self.k:
            heapq.heappushpop(self.q,val)

        return self.q[0]