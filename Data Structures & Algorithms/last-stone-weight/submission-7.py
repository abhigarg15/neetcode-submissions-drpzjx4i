class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # nums = [ -stone for stone in stones]
        # heapq.heapify(nums)
        # while len(nums) > 1:
        #     x = heapq.heappop(nums)
        #     y = heapq.heappop(nums)
        #     print(x,y)
        #     if abs(x-y) > 0:
        #         heapq.heappush(nums,-abs(x-y))
        #     # print(nums)
        
        # if nums:
        #     return -nums[0]
        
        # return 0

        # nums = []
        # for stone in stones:
        #     heapq.heappush(nums,-stone)

        # while len(nums) > 1:
        #     p = heapq.heappop(nums)
        #     q = heapq.heappop(nums)

        #     if abs(p-q) > 0:
        #         heapq.heappush(nums,-abs(p-q))

        # if nums:
        #     return -nums[0]

        # return 0


        # we need to create a max Heap because we want the largest weights first
        
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            A = -heapq.heappop(maxHeap)
            B = -heapq.heappop(maxHeap)

            if A != B:
                heapq.heappush(maxHeap, -abs(A-B))

        if maxHeap:
            return -heapq.heappop(maxHeap)

        return 0

