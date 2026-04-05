class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # o(n^2)
        # output = []
        # for i in range(len(nums)-k+1):
        #     maxVal = nums[i]
        #     for j in range(i,i+k):
        #         maxVal = max(nums[j],maxVal)
            
        #     output.append(maxVal)

        # return output

        # maxVal = float("-inf")
        # q = deque()
        # l = 0
        # output=[]
        # for r in range(len(nums)):
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()

        #     q.append(r)
        #     if l > q[0]:
        #         q.popleft()

        #     if r+1>=k:
        #         output.append(nums[q[0]])
        #         r+=1

        #     r+=1
        # return output


        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            if i >= k - 1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)

                output.append(-heap[0][0])
        return output


            