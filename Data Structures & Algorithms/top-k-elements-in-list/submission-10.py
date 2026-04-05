class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        Create Dictionary, store frequency of each element
        TC = O(n) This is wrong the TC is nlogn as we are sorting the elements inside the 
        dictionary to get it sorted based on values.

        SC = O(n)
        """

        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0)+1;
        # ans = []
        # # d = sorted(d, key = d.get, reverse= True) # this method returns the keys sorted by values
        # d = sorted(d.items(), key = lambda i: i[1], reverse = True)
        # for key,value in d:
        #     ans.append(key)
        #     k-=1
        #     if k == 0:
        #         break
        # return ans
        """
        Method 2: bucket sort can do this question in O(n) tc
        """

        bucket = [[] for _ in range(len(nums)+1)] # this is our bucket;
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1

        for ke,v in count.items():
            bucket[v].append(ke)
        
        ans = []
        for i in range(len(bucket)-1,0,-1):
            if len(bucket[i]) != 0 :
                for j in range(0,len(bucket[i])):
                    ans.append(bucket[i][j])
                    k-=1
            if k == 0 :
                break
        return ans



