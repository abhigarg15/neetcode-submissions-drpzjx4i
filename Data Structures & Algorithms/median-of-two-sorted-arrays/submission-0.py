class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ptr1 = 0
        ptr2 = 0

        res = []
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                res.append(nums1[ptr1])
                ptr1+=1
            else:
                res.append(nums2[ptr2])
                ptr2+=1


        while ptr1 < len(nums1):
            res.append(nums1[ptr1])
            ptr1+=1
        
        while ptr2 < len(nums2):
            res.append(nums2[ptr2])
            ptr2+=1

        n = len(res)
        if len(res)%2 == 0:
            return (res[n//2] + res[n//2-1])/2

        return res[n//2]

